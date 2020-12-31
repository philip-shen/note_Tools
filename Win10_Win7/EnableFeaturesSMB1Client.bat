echo SMB 1.0/CIFS ファイル共有のサポート：有効化
dism /online /Enable-Feature /FeatureName:SMB1Protocol /NoRestart
rem echo SMB 1.0/CIFS クライアント：無効化
rem ※今回はクライアントPCでSMBv1を利用するためコメントアウト化。
rem dism /online /Enable-Feature /FeatureName:SMB1Protocol-Client /NoRestart
echo SMB 1.0/CIFS サーバー：無効化
dism /online /Disable-Feature /FeatureName:SMB1Protocol-Server /NoRestart
echo SMB 1.0/CIFS 自動削除：無効化　バージョンによって自動削除が実装されていない場合があります。
dism /online /Disable-Feature /FeatureName:SMB1Protocol-Deprecation /NoRestart
echo このあとPCを再起動してください。
PAUSE