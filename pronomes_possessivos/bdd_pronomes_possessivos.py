

pro_pos = ['mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs']

pro_pos_pt_br = ['meu/minha', 'seu(a)', 'dele', 'dela', 'disso', 'nosso', 'deles(as)']

mine_ = ['mine', 'meu/minha']
yours_ = ['yours', 'seu(a)']
his_ = ['his', 'dele']
hers_ = ['hers', 'dela']
its_ = ['its', 'disso']
ours_ = ['ours', 'nosso']
theirs_ = ['theirs', 'deles(as)']


if __name__ == '__main__':
    bricks = '=' * 100

    print('\n')
    print(bricks)
    print(f'{len(pro_pos) = }')
    print(f'{len(pro_pos_pt_br) = }')

    print('\n')
    for word in zip(pro_pos, pro_pos_pt_br):
        print(word)

    print('\n')
    counter = 0
    while counter < len(pro_pos):
        print(f"{pro_pos[counter]}_ = ['{pro_pos[counter]}', '{pro_pos_pt_br[counter]}']")
        counter += 1
