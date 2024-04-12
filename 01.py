# CSV 読み込み read_csv
m_store = pd.read_csv('./drive/MyDrive/100pon_kikai/01/m_store.csv')
m_store

# 要素出力
len(m_store)

# 先頭 5 件出力
m_store.head()

# csv 読み込み
tbl_04 = pd.read_csv('./drive/MyDrive/100pon_kikai/01/tbl_order_202004.csv')
tbl_04

tbl_05 = pd.read_csv('./drive/MyDrive/100pon_kikai/01/tbl_order_202005.csv')
tbl_05

### データのユニオン（結合）
order_all = pd.concat([tbl_04, tbl_05], ignore_index=True)
order_all

# データ件数の比較
len(order_all) == len(tbl_04) + len(tbl_05)

##### カレントディレクトリのファイル一覧を表示
current_dir = os.getcwd()
current_dir

os.listdir(current_dir)