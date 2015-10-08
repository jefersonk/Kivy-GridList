# Kivy-GridList 
Código para uso livre

obs: O adapter utilizado deve ter largura limitada (ex: width:200, size_hint_x: None), para que caiba mais que uma coluna por linha.


Exemplo de adapter:
[CategoriesList@SelectableView+BoxLayout+Button]:
    size_hint: None, None
    height: 180
    width: 185
    index: ctx.index
    padding: 35,0,0,0
    background_normal:'static/imgs/products/background_white_vertical.png'
    background_down:'static/imgs/products/background_white_vertical.png'

    BoxLayout:
        size_hint:1,1
        orientation: 'vertical'

        AnchorLayout:
            anchor_y: 'center'
            anchor_x: 'center'
            size_hint: None, None
            pos: self.parent.pos
            width: 150
            height: 150
            canvas:
                Color:
                    rgba: (1,1,1,1)
                Rectangle:
                    source:'static/imgs/products/cat.png'
                    size: self.size
                    pos: self.pos

            Image:
                id: image_product
                source: ctx.image_path
                size_hint: None,None
                size: (140,140)

        LabelRegular:
            size_hint: None,None
            height: 20
            width: 150
            text: ctx.name
            color: 0,0,0,1
            font_size: '12sp'
