import dropbox
dropbox_access_token= "sl.BJhsJGsrJzQuARzbhso8BOkKum19STWKDqcMNs5KjbMyrsqfXKTpRIQqiodKxAl_JP6SfNHBLQ1feP16ZXB5FP3UBHMgTbSIXCW7epg1t2caIGB6NJqXMqF9tutZbCRteVzzYkjaLebE"
dropbox_path= "/sample.txt"
computer_path=r"D:\SEM 6\storage\sample.txt"
client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")
client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))
metadata, f = client.files_download('/sample.txt')
out = open("new.txt", 'wb')
out.write(f.content)
out.close()
print("[SUCCESS] downloaded")
