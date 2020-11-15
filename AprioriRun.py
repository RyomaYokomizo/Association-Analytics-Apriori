from mlxtend.frequent_patterns import apriori,association_rules
import numpy as np
import pandas as pd
import re

class AprioriRun():
    def __init__(self, file_name):
        self.file_name = file_name

    # ファイルを読み込む関数
    def read_file(self):
        if '.csv' in self.file_name:
            csv_file_df = pd.read_csv(self.file_name)
            return csv_file_df
        elif '.txt' in self.file_name:
            text_file_df = pd.read_table(self.file_name)
            return text_file_df

    #日付を表す変数が日付型ではない時のタイプ変更関数
    def change_date_type(self, date_valiable_name):
        read_file_df = AprioriRun.read_file(self)
        read_file_df[date_valiable_name] = pd.to_datetime(read_file_df[date_valiable_name])
        return read_file_df

    #　売上や購入数などの上位商品テーブル作成関数
    def generate_top_product_df(self, read_file_df, product_valiable_name, value_valiables_name, sort_value_valiable_name):
        file_df = read_file_df
        product_gp_df = file_df.groupby(product_valiable_name, as_index=False)[value_valiables_name].sum()
        product_gp_df = product_gp_df.sort_values(sort_value_valiable_name , ascending=False)
        return product_gp_df
    
    # Apriori(アソシエーション)実行関数
    def generate_apriori(self, read_file_df, index_valiable_name, columns_valiable_name, values_valiable_name, min_support_value):
        file_df = read_file_df
        basket = pd.pivot_table(data=file_df, index=index_valiable_name, columns=columns_valiable_name, values=values_valiable_name, aggfunc='sum', fill_value=0)
        basket = basket.apply(lambda x: x>0)
        # アプリオリによる分析
        freq_item = apriori(basket, min_support=min_support_value, use_colnames=True)
        # アソシエーションルールの抽出
        rules = association_rules(freq_item, metric='lift', min_threshold=1)
        # リフト値でソート
        rules = rules.sort_values('lift', ascending=False)
        return rules