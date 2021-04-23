import random


class Card():
    '''
    一张牌
    '''
    __slots__ = ('_face', '_suite')

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite
    
    def __str__(self):
        # 使用print函数时，默认打印该方法的返回值
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        ''' 
        关于__repr__方法：
        __str__是面向用户的，主要通过print函数输出；而__repr__面向程序员，此方法通常被用于调试时显示详细的对象信息，因此需要尽可能确保其包含丰富完整的信息且无歧义。

        什么情况下会触发__repr__方法呢？主要有如下情况会触发__repr__的调用：
        1. 在交互环境下直接输入对象名查看对象内容；
        2. 使用repr(对象)名查看对象内容；
        3. 直接调用“对象.repr()”方法；
        '''
        return self.__str__()

class Poker():
    '''
    一副牌
    '''

    __slots__ = ('_cards', '_current')

    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        '''洗牌'''
        self._current = 0
        random.shuffle(self._cards)
    
    @property
    def next(self):
        '''发牌'''
        # 洗过牌了，直接按顺序发就可以
        card = self._cards[self._current]
        self._current += 1
        return card
    
    @property
    def has_next(self):
        '''判断是否还有牌剩余'''
        # self._current是已经发下去的牌的数目
        # self._cards是总牌数
        return self._current < len(self._cards)

class Player():
    '''
    玩家
    '''

    __slots__ = ('_name', '_cards_on_hand')

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def cards_on_hand(self):
        return self._cards_on_hand
    
    def get(self, card):
        '''摸牌'''
        self._cards_on_hand.append(card)
    
    def arrange(self, card_key):
        '''玩家整理手上的牌'''
        self._cards_on_hand.sort(key=card_key)
        

def get_key(card):
    # 排序规则： 先根据花色，再根据点数排序
    # return (card.suite, card.face)
    # 排序规则： 先根据点数，再根据花色排序
    return (card.face, card.suite)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        # 整理手上的牌
        player.arrange(get_key)
        # 把整理好的牌打印出来
        print(player.cards_on_hand)

if __name__ == '__main__':
    main()
        


