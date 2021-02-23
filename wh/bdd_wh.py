

wh_gl = [
    'How', 'What', 'When', 'Where', 'Which', 'Who', 'Whose', 'Why',
    'how', 'what', 'when', 'where', 'which', 'who', 'whose', 'why'
]

wh_all_u = ['How', 'What', 'When', 'Where', 'Which', 'Who', 'Whose', 'Why']

wh_l = ['how', 'what', 'when', 'where', 'which', 'who', 'whose', 'why']
wh_l_pt_br = [
    'como/quão/quanto', 'o quê/qual(is)', 'quando', 'onde', 'que', 'que/quem (humano)', 'de quem',
    'porque', 'porquê'
]

wh_specific_u = ['How', 'Where', 'Who']
wh_specific_l = ['how', 'where', 'who']

if __name__ == '__main__':
    for word in zip(wh_l, wh_l_pt_br):
        print(word[0])
        print(word[1])
