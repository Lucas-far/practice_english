

pro = [
    'I', 'you', 'he', 'she', 'it', 'we', 'you', 'they',
    'I', 'You', 'He', 'She', 'It', 'We', 'You', 'They',
]

pro_u = ['I', 'You', 'He', 'She', 'It', 'We', 'You', 'They']

pro_l = ['I', 'you', 'he', 'she', 'it', 'we', 'you', 'they']

pro_pt_br = ['eu', 'tu/você', 'ele', 'ela', 'isso', 'nós', 'vós/vocês', 'eles(as)']

pro_sgl_u = ['I', 'He', 'She', 'It']

pro_sgl_l = ['I', 'he', 'she', 'it']

pro_sgl_is_u = ['He', 'She', 'It']

pro_sgl_is_l = ['he', 'she', 'it']

pro_pl_u = ['We', 'You', 'They']

pro_pl_l = ['we', 'you', 'they']

pro_pl_others_u = ['I', 'We', 'You', 'They']

pro_pl_others_l = ['I', 'we', 'you', 'they']

i_u, you_u, he_u, she_u, it_u, we_u, they_u = \
    ['I'], ['You'], ['He'], ['She'], ['It'], ['We'], ['They']

i_l, you_l, he_l, she_l, it_l, we_l, they_l = \
    ['I'], ['you'], ['he'], ['she'], ['it'], ['we'], ['they']

I_ = ['I', 'eu']
you_ = ['you', 'tu/você']
he_ = ['he', 'ele']
she_ = ['she', 'ela']
it_ = ['it', 'isso']
we_ = ['we', 'nós']
you__ = ['you', 'vós/vocês']
they_ = ['they', 'eles(as)']


if __name__ == '__main__':
    bricks = '=' * 100

    print('\n')

    print(bricks)
    print(f'{len(pro_l) = }')
    print(f'{len(pro_pt_br) = }')

    print('\n')
    for word in zip(pro_l, pro_pt_br):
        print(word)

    # counter = 0
    # while counter < len(pro_l):
    #     print(f"{pro_l[counter]}_ = ['{pro_l[counter]}', '{pro_pt_br[counter]}']")
    #     counter += 1
