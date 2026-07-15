def extensions(ext: str):
    match ext:
        case 'jpg':
            print('image/jpeg')
        case 'gif' | 'jpeg' | 'png':
            print(f'image/{ext}')
        case 'pdf' | 'zip':
            print(f'application/{ext}')
        case 'txt':
            print('text/plain')
        case _ :    
            print('application/octet-stream')

def main():
    # rpartition returns a tuple like (str before sep, sep, str after) STARTING FROM THE END
    _, dot, ext = input('Insert the name of your file: ').lower().strip().rpartition('.')
    extensions(ext)

main()