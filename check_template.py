import requests
from func_bin import get_bin_info

def checking_template(ccvip, msg, respuesta, gateway, tiempo, username, user_rank, proxyy):
    x = get_bin_info(ccvip[:6])

    return f"""<b>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Rox Chk
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Gateway ↯ <code>{gateway}</code>   
<b>- - - - - - - - - - - - - - - - - - - -</b>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] CC: <code>{ccvip}</code>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Status: <b>{msg}</b> 
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Response: {respuesta}
<b>- - - - - - - - - - - - - - - - - - - -</b>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Bin: <code>{x.get("type")}</code> | <code>{x.get("level")}</code> | <code>{x.get("vendor")}</code>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Country: <code>{x.get("country")} {x.get("flag")}</code>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Bank: <code>{x.get("bank_name")}</code>
<b>- - - - - - - - - - - - - - - - - - - -</b>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Proxy: <code>{proxyy}</code>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Time taken: <code>{tiempo} (segundos)</code>
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Checked by: @{username} [{user_rank}]
[<a href="https://t.me/RefeDarwinScrapper">⽷</a>] Bot by ↯ @Exzzex </b>"""