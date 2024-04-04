import os


class AllCornerCharacterProcessor():
    def __init__(self):
        self.all_corner_character_mp = {
            '０': '0',
            '１': '1',
            '２': '2',
            '３': '3',
            '４': '4',
            '５': '5',
            '６': '6',
            '７': '7',
            '８': '8',
            '９': '9',
        }

    def solve_character(self, c: str):
        assert len(c) == 1
        return self.all_corner_character_mp[c] if c in self.all_corner_character_mp else c

    def solve_file(self, input_file, output_file):

        ss = ''
        with open(input_file, 'r', encoding='utf-8') as f:
            for x in f.readlines():
                for c in x:
                    ss += self.solve_character(c)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(ss)

    def solve_folder(self, input_folder, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        cnt = 0
        for filename in os.listdir(input_folder):
            if filename.endswith('.txt'):
                print(cnt, filename)
                self.solve_file(os.path.join(input_folder, filename),
                                os.path.join(output_folder, filename))
                cnt += 1


if __name__ == '__main__':
    input_folder = r'D:\APersonal\Agraduate\AinGroup\research\突发事件NER\数据\CEC-Corpus\raw corpus\allSourceText'
    output_folder = r'D:\APersonal\Agraduate\AinGroup\AProjects\NER\generate_data\CEC-Corpus_solved2'
    allCornerCharacterProcessor = AllCornerCharacterProcessor()
    allCornerCharacterProcessor.solve_folder(input_folder, output_folder)
