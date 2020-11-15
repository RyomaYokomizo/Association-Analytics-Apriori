from  AprioriRun import AprioriRun
import sys

if __name__== '__main__':
  #テキストファイルと店舗名入力
    #sys.argv[1]=ファイル名
    apriori_run = AprioriRun(sys.argv[1])
    #sys.argv[2]=日付変数名
    read_file_df = apriori_run.change_date_type(sys.argv[2])
    #sys.argv[3]=商品変数名, sys.argv[4]=値変数名
    product_gp_df = apriori_run.generate_top_product_df(read_file_df, sys.argv[3], sys.argv[4], sys.argv[4])
    #sys.argv[5]=インデックス変数名sys.argv[6]=最低サポート値
    rules = apriori_run.generate_apriori(read_file_df, sys.argv[5], sys.argv[3], sys.argv[4], float(sys.argv[6]))
    rules.to_csv(sys.argv[7], encoding='utf-8')
