import webbrowser
url = "https://www.youtube.com/watch?v=tJGBVigwPlU&list=RDMMtJGBVigwPlU&start_radio=1"
download = url[:12] + "ss" + url[12:]

webbrower.open(download)