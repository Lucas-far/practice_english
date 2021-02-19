

colors: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

if __name__ == '__main__':
    print(colors[0] + 'texto' + colors[7])
    print(colors[1] + 'texto' + colors[7])
    print(colors[2] + 'texto' + colors[7])
    print(colors[3] + 'texto' + colors[7])
    print(colors[4] + 'texto' + colors[7])
    print(colors[5] + 'texto' + colors[7])
    print(colors[6] + 'texto' + colors[7])
