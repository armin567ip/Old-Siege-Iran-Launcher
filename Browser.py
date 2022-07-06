import webview
if __name__ == '__main__':
    webview.create_window('Old Siege',
                          'http://localhost:8501/',
                          min_size=(1383, 800)
                          )
    webview.start()
