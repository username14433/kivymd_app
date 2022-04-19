from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

KV = '''
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LibraryScreen:
    TimetableScreen:
    NavigationScreen:
    SettingsScreen:
    SafetyMethodsScreen:
    BuffetScreen:
    TestScreen:
    SafetyTestScreen:
    TestterScreen:
    TesttbScreen:
    TestofScreen:
    TesttfScreen:
    TestthfScreen:
    TestotScreen:
    TestttScreen:
    TestthtScreen:
    TestotbScreen:
    BuffetScreen:
    CorrectScreen:
    WrongScreen:
    Klassdes:
    Klassdesd:
    Klassdesg:
    Klassdesv:
    Klassodinna:
    Klassodinnb:
    Klassodinnv:
    Klassodinng:
    Klassodinnd:
    Klassdeve:
    Klassdevz:
    Klassdesb:
    
    
<WelcomeScreen>:
    name: 'welcome'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1


    MDIconButton:
        icon: 'utilits/School Assistant.png'
        user_font_size: "300sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        on_press: root.manager.current = 'main'
    MDLabel:
        halign: 'center'
        text: "School Assistant"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
        
<MainScreen>:
    name: 'main'
    MDBoxLayout:
        md_bg_color: 1, 1, 1, 1
        MDCard:
            pos_hint: {'center_x': 0.5, 'center_y': 1.1}
            md_bg_color: .35, 0, .56, 1
            radius: [40,] 
            border_radius: 40
    MDIconButton:
        icon: 'utilits/School Assistant.png'
        pos_hint: {'center_x': 0.035, 'center_y': 0.93}  
        user_font_size: "75sp"
        on_press: root.manager.current = 'welcome'        
    MDLabel:
        text: "Main"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
        pos_hint: {'center_x': 0.98, 'center_y': 0.945}
    MDLabel:
        text: "School Assistant"
        font_style: 'Button'
        font_size: "65sp"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        pos_hint: {'center_x': 0.845, 'center_y': 0.75}
    MDLabel:
        text: "Навигация"
        font_style: 'Button'
        font_size: "15sp"
        theme_text_color: "Custom"
        text_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.972, 'center_y': 0.369}
    MDLabel:
        text: "Библиотека"
        font_style: 'Button'
        font_size: "15sp"
        theme_text_color: "Custom"
        text_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.77, 'center_y': 0.57}
    MDLabel:
        text: "Расписание"
        font_style: 'Button'
        font_size: "15sp"
        theme_text_color: "Custom"
        text_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 1.168, 'center_y': 0.57}
    MDIconButton :
        icon : "utilits/Library.png"
        pos_hint : {"center_x": 0.3,"center_y": .45}
        user_font_size : 150
        theme_text_color : "Custom"
        text_color : [0,0,1,1]
        on_press : self.text_color = [1,0,0,1]
        on_release : self.text_color = [0,0,1,1]
        text_color : [0,0,1,1]
        on_press: root.manager.current = 'library'
    MDIconButton:
        icon: 'utilits/Navigation.png'
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        user_font_size : 150
        theme_text_color : "Custom"
        text_color : [0,0,1,1]
        on_press : self.text_color = [1,0,0,1]
        on_release : self.text_color = [0,0,1,1]
        text_color : [0,0,1,1]
        on_press: root.manager.current = 'navigation'
    MDIconButton:
        icon: 'utilits/timetable.png'
        pos_hint: {'center_x': 0.7, 'center_y': 0.45}
        user_font_size : 150
        theme_text_color : "Custom"
        text_color : [0,0,1,1]
        on_press : self.text_color = [1,0,0,1]
        on_release : self.text_color = [0,0,1,1]
        text_color : [0,0,1,1]
        on_press: root.manager.current = 'timetable'  
    MDFillRoundFlatIconButton:
        text: 'Техника безопасности'
        pos_hint: {'center_x': 0.5, 'center_y': 0.65}
        md_bg_color:  0.63, 0, 1, 1
        icon: 'alert'     
        font_size: '35sp'
        on_press: root.manager.current = 'safety'
    MDIconButton:
        icon: 'utilits/Settings.png'
        user_font_size: "50sp" 
        pos_hint: {'center_x': 0.97, 'center_y': 0.95}
        on_press: root.manager.current = 'settings'
    MDFillRoundFlatIconButton:
        icon: 'pizza'
        text: 'Хотите сделать заказ?'
        md_bg_color:  0.63, 0, 1, 1
        font_size: '45sp'
        pos_hint: {'center_x': 0.51, 'center_y': 0.08}
        on_press: root.manager.current = 'buffet'  


<SettingsScreen>:
    name: 'settings'
    MDBoxLayout:
        id: 'main_box_layout'
        md_bg_color:  .35, 0, .56, 1
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'main'
    MDLabel:
        text: 'Settings'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
        pos_hint: {'center_x': 0.95, 'center_y': 0.900}
    MDCard:
        id: 'head_down_circle'
        radius: [100, ]
        border_radius: 100
        pos_hint: {'center_x': 0.995, 'center_y': 0.05}
        md_bg_color: 0.63, 0, 1, 1
        size_hint: None, None
        size: "200dp", "200dp"
    MDCard:
        id: 'box_for_body_switches'
        radius: [100, ]
        border_radius: 100
        pos_hint: {'center_x': 0.2, 'center_y': 0.1}
        md_bg_color: 1, 1, 1, 1
        size_hint: None, None
        size: "1450dp", "600dp"
    MDCard:
        id: 'head_up_circle'
        radius: [100, ]
        border_radius: 100
        pos_hint: {'center_x': 0.975, 'center_y': 0.95}
        md_bg_color: 0.63, 0, 1, 1
        size_hint: None, None
        size: "200dp", "200dp"
    MDCard:
        id: 'head_box_for_switch1'
        radius: [45, ]
        border_radius: 45
        size_hint: None, None
        size: "650dp", "80dp"
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.45, 'center_y': 0.77}
    MDCard:
        id: 'head_box_for_switch2'
        radius: [45, ]
        border_radius: 45
        size_hint: None, None
        size: "650dp", "80dp"
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.45, 'center_y': 0.63}
    MDCard:
        id: 'body_box_for_switch1'
        radius: [40, ]
        border_radius: 40
        size_hint: None, None
        size: "770dp", "70dp"
        md_bg_color: .35, 0, .56, 1
        pos_hint: {'center_x': 0.34, 'center_y': 0.38}
    MDCard:
        id: 'body_box_for_switch2'
        radius: [40, ]
        border_radius: 40
        size_hint: None, None
        size: "770dp", "70dp"
        md_bg_color: .35, 0, .56, 1
        pos_hint: {'center_x': 0.34, 'center_y': 0.23}
    MDCard:
        id: 'body_box_for_switch3'
        radius: [40, ]
        border_radius: 40
        size_hint: None, None
        size: "770dp", "70dp"
        md_bg_color: .35, 0, .56, 1
        pos_hint: {'center_x': 0.34, 'center_y': 0.08}
    MDSwitch:
        id: 'head_switch1'
        pos_hint: {'center_x': 0.63, 'center_y': 0.77}
        width: dp(45)
    MDLabel:
        id: 'head_switch_label1'
        text: 'Отключить уведомления'
        pos_hint: {'center_x': 0.8, 'center_y': 0.77}
    MDSwitch:
        id: 'head_switch2'
        pos_hint: {'center_x': 0.63, 'center_y': 0.63}
        width: dp(45)
        on_active: self.theme_cls.theme_style = 'Dark'
    MDLabel:
        id: 'head_switch_label2'
        text: 'Тёмная тема'
        pos_hint: {'center_x': 0.8, 'center_y': 0.63}
    MDSwitch:
        id: 'body_switch1'
        pos_hint: {'center_x': 0.56, 'center_y': 0.08}
        width: dp(45)
    MDLabel:
        id: 'body_switch_label1'
        text: '#1'
        pos_hint: {'center_x': 0.64, 'center_y': 0.38}
    MDSwitch:
        id: 'body_switch2'
        pos_hint: {'center_x': 0.56, 'center_y': 0.23}
        width: dp(45)
    MDLabel:
        id: 'body_switch_label2'
        text: '#2'
        pos_hint: {'center_x': 0.64, 'center_y': 0.23}
    MDSwitch:
        id: 'body_switch3'
        pos_hint: {'center_x': 0.56, 'center_y': 0.38}
        width: dp(45)
    MDLabel:
        id: 'body_switch_label3'
        text: '#3'
        pos_hint: {'center_x': 0.64, 'center_y': 0.08}


<LibraryScreen>:
    name: 'library'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/Circle.png'
        md_bg_color:  0.63, 0, 1, 1
        user_font_size: "250sp" 
        pos_hint: {'center_x': 0.99, 'center_y': 0.97}
    MDIconButton:
        icon: 'utilits/Library_img.png'
        user_font_size: "500sp"
        pos_hint: {'center_x': 0.52, 'center_y': 0.48}
    MDIconButton:
        icon: 'utilits/School Assistant.png'
        pos_hint: {'center_x': 0.035, 'center_y': 0.93}  
        user_font_size: "75sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/Circle.png'
        pos_hint: {'center_x': 0.0005, 'center_y': 0.55}  
        user_font_size: "250sp"
    MDIconButton:
        icon: 'utilits/Circle.png'
        pos_hint: {'center_x': 1, 'center_y': 0.005}  
        user_font_size: "250sp"         
    MDLabel:
        text: "Library"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
        pos_hint: {'center_x': 0.98, 'center_y': 0.945}
    MDIconButton:
        icon: 'utilits/img_9.png'
        icon_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.57}
        user_font_size : 200
        theme_text_color : "Custom"
        text_color : [0,0,1,1]
        on_press : self.text_color = [1,0,0,1]
        on_release : self.text_color = [0,0,1,1]
        text_color : [0,0,1,1]
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.15}
        size_hint: None, None
        size: "380dp", "100dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: '[ref=some]Перейти в базу данных [/ref]'
            color: 1,1,1,1 
            font_style: 'H3'
            font_size:"40sp"
            halign: 'center'
            on_ref_press:
                import webbrowser 
                webbrowser.open('https://schoolassistant512.sharepoint.com/sites/SchoolAssistant/Lists/List4/AllItems.aspx?skipSignal=true') 


<TimetableScreen>:
    name: 'timetable'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDFillRoundFlatIconButton:
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.97}
        on_press: root.manager.current = 'main'    
# Украшенияя справа
    MDIconButton:
        icon: 'utilits/Circle1.png'
        user_font_size: "100sp" 
        pos_hint: {'center_x': 1.05, 'center_y': 0.95}
    MDIconButton:
        icon: 'utilits/Circle1.png'
        user_font_size: "120sp" 
        pos_hint: {'center_x': 1.08, 'center_y': 0.54}
    MDIconButton:
        icon: 'utilits/Circle1.png'
        user_font_size: "130sp" 
        pos_hint: {'center_x': 1.05, 'center_y': 0.01}
# Номера Классов (фон)
    MDIconButton:
        icon: 'utilits/11klass.png'
        user_font_size: "100sp" 
        pos_hint: {'center_x': 0.155, 'center_y': 0.15}
    MDIconButton:
        icon: 'utilits/SquareWhite.png'
        user_font_size: "120sp" 
        pos_hint: {'center_x': 0.155, 'center_y': 0.445}
    MDIconButton:
        icon: 'utilits/10klass.png'
        user_font_size: "100sp" 
        pos_hint: {'center_x': 0.155, 'center_y': 0.45}
    MDIconButton:
        icon: 'utilits/9klass.png'
        user_font_size: "100sp" 
        pos_hint: {'center_x': 0.155, 'center_y': 0.75}
#Квадратики под буквами 9 классов
    MDIconButton:
        icon: 'utilits/LetterA.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.45, 'center_y': 0.8}
        on_press: root.manager.current = 'settings'
    MDIconButton:
        icon: 'utilits/LetterB.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.60, 'center_y': 0.8}
    MDIconButton:
        icon: 'utilits/LetterV.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.75, 'center_y': 0.8}
        on_press: root.manager.current = 'settings'
    MDIconButton:
        icon: 'utilits/LetterG.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.90, 'center_y': 0.8}
    MDIconButton:
        icon: 'utilits/LetterD.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.45, 'center_y': 0.7}
    MDIconButton:
        icon: 'utilits/LetterE.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.60, 'center_y': 0.7}
        on_press: root.manager.current = 'settings'
    MDIconButton:
        icon: 'utilits/LetterZ.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.75, 'center_y': 0.7}
        on_press: root.manager.current = 'raspisaniedevz'
#Квадратики под 10 классы
    MDIconButton:
        icon: 'utilits/LetterA.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.45, 'center_y': 0.5}
        on_press: root.manager.current = 'raspisaniedesa'
    MDIconButton:
        icon: 'utilits/LetterB.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.60, 'center_y': 0.5}
        on_press: root.manager.current = 'raspisaniedesb'
    MDIconButton:
        icon: 'utilits/LetterV.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.75, 'center_y': 0.5}
        on_press: root.manager.current = 'raspisaniedesv'
    MDIconButton:
        icon: 'utilits/LetterG.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.45, 'center_y': 0.4}
        on_press: root.manager.current = 'raspisaniedesg'
    MDIconButton:
        icon: 'utilits/LetterDW.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.60, 'center_y': 0.4}
        on_press: root.manager.current = 'raspisanie'
#Квадратики под 11 классы
    MDIconButton:
        icon: 'utilits/LetterA.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.45, 'center_y': 0.2}
        on_press: root.manager.current = 'raspisanieodinna'
    MDIconButton:
        icon: 'utilits/LetterB.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.60, 'center_y': 0.2}
        on_press: root.manager.current = 'raspisanieodinnb'
    MDIconButton:
        icon: 'utilits/LetterV.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.75, 'center_y': 0.2}
        on_press: root.manager.current = 'raspisanieodinnv'
    MDIconButton:
        icon: 'utilits/LetterG.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.45, 'center_y': 0.1}
        on_press: root.manager.current = 'raspisanieodinng'
    MDIconButton:
        icon: 'utilits/LetterDW.png'
        user_font_size: "25sp" 
        pos_hint: {'center_x': 0.60, 'center_y': 0.1}
        on_press: root.manager.current = 'raspisanieodinnd'


#Надпись по центру сверху
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.50, 'center_y': 0.90}
        size_hint: None, None
        size: "250dp", "45dp"
        radius: [30, ]
        border_radius: 30 
        MDLabel:
            halign:'center'
            text:'Ваш класс'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: 'H3'   
#Само расписание 10 классы
<Klassdesd>:
    name: 'raspisanie'
    
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1
    
        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/10dMon.png"

            Image:
                source:"utilits/10dTue.png"

            Image:
                source:"utilits/10dWed.png"

            Image:
                source:"utilits/10dThu.png"

            Image:
                source:"utilits/10dFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'

<Klassdesg>:
    name: 'raspisaniedesg'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/10gMon.png"

            Image:
                source:"utilits/10gTue.png"

            Image:
                source:"utilits/10gWed.png"

            Image:
                source:"utilits/10gThu.png"

            Image:
                source:"utilits/10gFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
<Klassdesv>:
    name: 'raspisaniedesv'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/10vMon.png"

            Image:
                source:"utilits/10vTue.png"

            Image:
                source:"utilits/10vWed.png"

            Image:
                source:"utilits/10vThu.png"

            Image:
                source:"utilits/10vFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
<Klassdesb>:
    name: 'raspisaniedesb'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/10bMon.png"

            Image:
                source:"utilits/10bTue.png"

            Image:
                source:"utilits/10bWed.png"

            Image:
                source:"utilits/10bThu.png"

            Image:
                source:"utilits/10bFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
<Klassdes>:
    name: 'raspisaniedesa'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/10aMon.png"

            Image:
                source:"utilits/10aTue.png"

            Image:
                source:"utilits/10aWed.png"

            Image:
                source:"utilits/10aThu.png"

            Image:
                source:"utilits/10aFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
#11 Класс само расписание

<Klassodinnd>:
    name: 'raspisanieodinnd'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/11dMon.png"

            Image:
                source:"utilits/11dTue.png"

            Image:
                source:"utilits/11dWed.png"

            Image:
                source:"utilits/11dThu.png"

            Image:
                source:"utilits/11dFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
<Klassodinng>:
    name: 'raspisanieodinng'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/11gMon.png"

            Image:
                source:"utilits/11gTue.png"

            Image:
                source:"utilits/11gWed.png"

            Image:
                source:"utilits/11gThu.png"

            Image:
                source:"utilits/11gFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
<Klassodinnv>:
    name: 'raspisanieodinnv'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/11vMon.png"

            Image:
                source:"utilits/11vTue.png"

            Image:
                source:"utilits/11vWed.png"

            Image:
                source:"utilits/11vThu.png"

            Image:
                source:"utilits/11vFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
<Klassodinnb>:
    name: 'raspisanieodinnb'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/11bMon.png"

            Image:
                source:"utilits/11bTue.png"

            Image:
                source:"utilits/11bWed.png"

            Image:
                source:"utilits/11bThu.png"

            Image:
                source:"utilits/11bFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
<Klassodinna>:
    name: 'raspisanieodinna'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/11aMon.png"

            Image:
                source:"utilits/11aTue.png"

            Image:
                source:"utilits/11aWed.png"

            Image:
                source:"utilits/11aThu.png"

            Image:
                source:"utilits/11aFri.png"
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
#9 классы расписание

<Klassdevz>:
    name: 'raspisaniedevz'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/9zMon.png"

            Image:
                source:"utilits/9zTue.png"

            Image:
                source:"utilits/9zWed.png"

            Image:
                source:"utilits/9zThu.png"

            Image:
                source:"utilits/9zFri.png"                
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'
<Klassdeve>:
    name: 'raspisaniedeve'
    MDBoxLayout:
        orientation:"vertical"
        size: root.width, root.height
        md_bg_color: .35, 0, .56, 1

        Carousel:
            direction:"bottom"
            Image:
                source:"utilits/9eMon.png"

            Image:
                source:"utilits/9eTue.png"

            Image:
                source:"utilits/9eWed.png"

            Image:
                source:"utilits/9eThu.png"

            Image:
                source:"utilits/9eFri.png"      
    MDFillRoundFlatIconButton:
        id: 'back_button_icon'
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'timetable'               
                
    
<NavigationScreen>:
    name: 'navigation'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDFillRoundFlatIconButton:
        icon: 'arrow-left'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'main'
    MDCard:
        pos_hint: {'center_x': 0.75, 'center_y': 0.5}
        size_hint: None, None
        size: 750, 750
        md_bg_color: 1, 1, 1, 1
        radius: [50,]
        border_radius: 50
    MDCard:
        pos_hint: {'center_x': 0.25, 'center_y': 0.8}
        size_hint: None, None
        size: 500, 100
        md_bg_color: 1, 1, 1, 1
        radius: [50,]
        border_radius: 50
    MDCard:
        pos_hint: {'center_x': 0.25, 'center_y': 0.6}
        size_hint: None, None
        size: 500, 100
        md_bg_color: 1, 1, 1, 1
        radius: [50,]
        border_radius: 50
    MDCard:
        pos_hint: {'center_x': 0.25, 'center_y': 0.4}
        size_hint: None, None
        size: 500, 100
        md_bg_color: 1, 1, 1, 1
        radius: [50,]
        border_radius: 50
    MDCard:
        pos_hint: {'center_x': 0.25, 'center_y': 0.2}
        size_hint: None, None
        size: 500, 100
        md_bg_color: 1, 1, 1, 1
        radius: [50,]
        border_radius: 50

<SafetyMethodsScreen>:
    name: 'safety'
    MDLabel:
        text: 'SafetyMethods'
        halign: 'center'
    MDFillRoundFlatIconButton:
        icon: 'utilits/человечек.png'
        text: 'Назад'
        md_bg_color:  0.63, 0, 1, 1
        pos_hint: {'center_x': 0.05, 'center_y': 0.9}
        on_press: root.manager.current = 'main'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/img_6.png'
        pos_hint: {'center_x': 0.975, 'center_y': 0.95}
        user_font_size: "200sp"
    MDIconButton:
        icon: 'utilits/School Assistant.png'
        pos_hint: {'center_x': 0.08, 'center_y': 0.72}
        user_font_size: "150sp"
    MDIconButton:
        icon: 'utilits/School Assistant.png'
        pos_hint: {'center_x': 0.08, 'center_y': 0.72}
        user_font_size: "100sp"
    MDIconButton:
        icon: "utilits/icons8-правила-96 1.png"
        pos_hint: {'center_x': 0.08, 'center_y': 0.72}
        user_font_size: "75sp"
    MDLabel:
        text: "Техника"
        font_style: 'Button'
        font_size: "30sp"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        pos_hint: {'center_x': 0.54, 'center_y': 0.58}
    MDLabel:
        text: "Безопастности"
        font_style: 'Button'
        font_size: "30sp"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        pos_hint: {'center_x': 0.507, 'center_y': 0.53}
    MDIconButton:
        icon: 'utilits/img_6.png'
        pos_hint: {'center_x': 0.995, 'center_y': 0.05}
        user_font_size: "200sp"
    MDLabel:
        text: "Safety Precautions"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.9, 'center_y': 0.945}
    MDIconButton:
        icon: "utilits/человечек.png"
        pos_hint: {'center_x': 0.965, 'center_y': 0.93}
        user_font_size: "50sp"
        on_press: root.manager.current = 'main'
    MDCard: 
        md_bg_color: 0.63, 0, 1, 1
        radius: [50,]
        border_radius: 50
        size_hint: None, None
        size: 700, 250
        pos_hint: {'center_x': 0.95, 'center_y': 0.6}
    MDCard: 
        md_bg_color: 1, 1, 1, 1
        radius: [50,]
        border_radius: 50
        size_hint: None, None
        size: 1450, 600
        pos_hint: {'center_x': 0.2, 'center_y': 0.1}
    MDIconButton:
        icon: 'utilits/School Assistant.png'
        pos_hint: {'center_x': 0.035, 'center_y': 0.93} 
        user_font_size: "75sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/img_12.png'
        pos_hint: {'center_x': 0.1, 'center_y': 0.12}
        user_font_size: "150sp"
    MDIconButton:
        icon: 'utilits/img_6.png'
        pos_hint: {'center_x': 0.1, 'center_y': 0.12}
        user_font_size: "100sp"

    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.1, 'center_y': 0.13}
        user_font_size: "55sp"
        on_press: root.manager.current = 'safety_test'
    MDLabel:
        text: "Пожар"
        theme_text_color: "Custom"
        text_color: .35, 0, .56, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.55, 'center_y': 0.27}    

    MDIconButton:
        icon: 'utilits/img_6.png'
        pos_hint: {'center_x': 0.3, 'center_y': 0.25}
        user_font_size: "150sp"
    MDIconButton:
        icon: 'utilits/img_12.png'
        pos_hint: {'center_x': 0.3, 'center_y': 0.25}
        user_font_size: "100sp"
    MDIconButton:
        icon: 'utilits/icons8-пистолет-100 1 (1).png'
        pos_hint: {'center_x': 0.3, 'center_y': 0.25}
        user_font_size: "75sp"
    MDLabel:
        text: "Теракт"
        theme_text_color: "Custom"
        text_color: .35, 0, .56, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.749, 'center_y': 0.11}  
    MDCard: 
        md_bg_color: .35, 0, .56, 1
        radius: [20,]
        border_radius: 20
        size_hint: None, None
        size: 1720, 75
        pos_hint: {'center_x': 0.12, 'center_y': 0.35}
    MDLabel:
        text: "Действия в случае ЧП"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.65, 'center_y': 0.35}
    MDFillRoundFlatButton:
        md_bg_color: .35, 0, .56, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.87, 'center_y': 0.7}
        text: "Пройти тест         "
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'Test'
    MDIconButton:
        icon: 'utilits/icons8-правила-96 1.png'
        pos_hint: {'center_x': 0.95, 'center_y': 0.7}
        user_font_size: "30sp"
        on_press: root.manager.current = 'Test'
    MDFillRoundFlatButton:
        md_bg_color: .35, 0, .56, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.87, 'center_y': 0.6}
        text: "Пройти тест         "
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.95, 'center_y': 0.6}
        user_font_size: "25sp"
    MDFillRoundFlatButton:
        md_bg_color: .35, 0, .56, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.87, 'center_y': 0.5}
        text: "Пройти тест         "
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
    MDIconButton:
        icon: 'utilits/icons8-пистолет-100 1 (1).png'
        pos_hint: {'center_x': 0.95, 'center_y': 0.5}
        user_font_size: "25sp"
        on_press: root.manager.current = 'Test'


<BuffetScreen>:
    name: 'buffet'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/img_16.png'
        md_bg_color:  0.63, 0, 1, 1
        user_font_size: "250sp" 
        pos_hint: {'center_x': 0.99, 'center_y': 0.97}
    MDIconButton:
        icon: 'utilits/img_13.png'
        user_font_size: "500sp"
        pos_hint: {'center_x': 0.52, 'center_y': 0.48}
    MDIconButton:
        icon: 'utilits/School Assistant.png'
        pos_hint: {'center_x': 0.035, 'center_y': 0.93}  
        user_font_size: "75sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/img_6.png'
        pos_hint: {'center_x': 0.0005, 'center_y': 0.55}  
        user_font_size: "250sp"
    MDIconButton:
        icon: 'utilits/img_6.png'
        pos_hint: {'center_x': 1, 'center_y': 0.005}  
        user_font_size: "250sp"         
    MDLabel:
        text: "Buffet"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
        pos_hint: {'center_x': 0.98, 'center_y': 0.945}
    MDIconButton:
        icon: 'utilits/img_2.png'
        icon_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.57}
        user_font_size : 200
        theme_text_color : "Custom"
        text_color : [0,0,1,1]
        on_press : self.text_color = [1,0,0,1]
        on_release : self.text_color = [0,0,1,1]
        text_color : [0,0,1,1]
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.15}
        size_hint: None, None
        size: "380dp", "100dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: '[ref=some]Перейти в телеграмм[/ref]'
            color: 1,1,1,1 
            font_style: 'H3'
            font_size:"40sp"
            halign: 'center'
            on_ref_press:
                import webbrowser 
                webbrowser.open('https://t.me/Bulat_1_bot')      

<SafetyTestScreen>:
    name: 'safety_test'
    MDBoxLayout:
        md_bg_color: 0, 0, 0, 1 
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True

    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        padding: 10, 10
        text: 'really some amazing text' * 1500
    
<TestScreen>: 
    name: 'Test'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDFillRoundFlatIconButton:
        icon: 'utilits/человечек.png'
        text: 'Назад'
        user_font_size : 180
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.1, 'center_y': 0.9}
        on_press: root.manager.current = 'main'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        text: "Тест 1"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'testof'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        text: "Тест 2"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'testtf'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        text: "Тест 3"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'testthf'
    MDLabel:
        text: "Выберете тест"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.9, 'center_y': 0.9}
        
        
        
<TestterScreen>: 
    name: 'TestterScreen'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDFillRoundFlatIconButton:
        icon: 'utilits/человечек.png'
        text: 'Назад'
        user_font_size : 180
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.1, 'center_y': 0.9}
        on_press: root.manager.current = 'main'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        text: "Тест 1"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'testot'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        text: "Тест 2"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'testtt'
        
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        text: "Тест 3"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'testtht'
    
    MDLabel:
        text: "Выберете тест"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.9, 'center_y': 0.9}



<TesttbScreen>: 
    name: 'TesttbScreen'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDFillRoundFlatIconButton:
        icon: 'utilits/человечек.png'
        text: 'Назад'
        user_font_size : 180
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.1, 'center_y': 0.9}
        on_press: root.manager.current = 'main'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        text: "Тест 1"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'testotb'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        text: "Тест 2"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        

    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "40sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        text: "Тест 3"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        

    MDLabel:
        text: "Выберете тест"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.9, 'center_y': 0.9}



<TestofScreen>: 
    name: 'testof'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/schoolassistaint.png'
        pos_hint: {'center_x': 0.06, 'center_y': 0.9}
        user_font_size: "110sp"
        on_press: root.manager.current = 'main'
    MDLabel:
        text: "Вопрос"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.95, 'center_y': 0.9}
    MDIconButton:
        icon: 'utilits/ntktuf1.png'
        pos_hint: {'center_x': 0.97, 'center_y': 0.95}
        user_font_size: "200sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.96, 'center_y': 0.94}
        user_font_size: "50sp"
        on_press: root.manager.current = 'main'
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.72}
        size_hint: None, None
        size: "300dp", "150dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: 'Причины возникновения пожаров в жилых и общественных зданиях (несколько вариантов ответа)'
            color: 1,1,1,1
            font_style: 'H3'
            font_size:"20sp"
            halign: 'center'
    MDCard: 
        md_bg_color: 0.63, 0, 1, 1
        radius: [20,]
        border_radius: 20
        size_hint: None, None
        size: 1720, 70
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        text: "неисправность электросети и электроприборов"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'correct'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        text: "осторожное обращение с огнем"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        text: "наличие первичных средств пожаротушения"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'


<TesttfScreen>: 
    name: 'testtf'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/schoolassistaint.png'
        pos_hint: {'center_x': 0.07, 'center_y': 0.9}
        user_font_size: "50sp"
        on_press: root.manager.current = 'main'
    MDLabel:
        text: "Вопрос"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.75, 'center_y': 0.9}
    MDIconButton:
        icon: 'utilits/ntktuf1.png'
        pos_hint: {'center_x': 0.97, 'center_y': 0.95}
        user_font_size: "90sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.94, 'center_y': 0.94}
        user_font_size: "25sp"
        on_press: root.manager.current = 'main'
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.72}
        size_hint: None, None
        size: "250dp", "100dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: 'Электроприборы под напряжение можно тушить при помощи огнетушителя'
            color: 1,1,1,1
            font_style: 'H3'
            font_size:"20sp"
            halign: 'center'
    MDCard: 
        md_bg_color: 0.63, 0, 1, 1
        radius: [20,]
        border_radius: 20
        size_hint: None, None
        size: 1720, 70
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        text: "Воздушно- пенного"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        text: "Углекислотного"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'correct'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        text: "Порошкового"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
        
        

<TestthfScreen>: 
    name: 'testthf'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/schoolassistaint.png'
        pos_hint: {'center_x': 0.07, 'center_y': 0.9}
        user_font_size: "50sp"
        on_press: root.manager.current = 'main'
    MDLabel:
        text: "Вопрос"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.75, 'center_y': 0.9}
    MDIconButton:
        icon: 'utilits/ntktuf1.png'
        pos_hint: {'center_x': 0.97, 'center_y': 0.95}
        user_font_size: "90sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.94, 'center_y': 0.94}
        user_font_size: "25sp"
        on_press: root.manager.current = 'main'
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.72}
        size_hint: None, None
        size: "250dp", "100dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: 'Какие положительные стороны есть у паники в чрезвычайной ситуации?'
            color: 1,1,1,1
            font_style: 'H3'
            font_size:"20sp"
            halign: 'center'
    MDCard: 
        md_bg_color: 0.63, 0, 1, 1
        radius: [20,]
        border_radius: 20
        size_hint: None, None
        size: 1720, 70
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        text: "Паника ускоряет реакцию"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        text: "Паника помогает легче переносить болевые ощущения"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        text: "У паники нет никаких плюсов, есть только минусы"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'correct'
        
        
        
<TestotScreen>: 
    name: 'testot'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/schoolassistaint.png'
        pos_hint: {'center_x': 0.06, 'center_y': 0.9}
        user_font_size: "100sp"
        on_press: root.manager.current = 'main'
    MDLabel:
        text: "Вопрос"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.95, 'center_y': 0.9}
    MDIconButton:
        icon: 'utilits/ntktuf1.png'
        pos_hint: {'center_x': 0.97, 'center_y': 0.95}
        user_font_size: "100sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.96, 'center_y': 0.94}
        user_font_size: "30sp"
        on_press: root.manager.current = 'main'
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.72}
        size_hint: None, None
        size: "300dp", "150dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: 'Что следует сделать при обнаружении подозрительного предмета?'
            color: 1,1,1,1
            font_style: 'H3'
            font_size:"20sp"
            halign: 'center'
    MDCard: 
        md_bg_color: 0.63, 0, 1, 1
        radius: [20,]
        border_radius: 20
        size_hint: None, None
        size: 1720, 70
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        text: "Взять его домой, чтобы лучше его сохранить до приезда специалистов"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        text: "Позвать друзей и рассмотреть его вместе"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        text: "Не трогать его, предупредить окружающих, сообщить о находке полиции"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'correct'
        
        
        
        
<TestttScreen>: 
    name: 'testtt'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/schoolassistaint.png'
        pos_hint: {'center_x': 0.06, 'center_y': 0.9}
        user_font_size: "100sp"
        on_press: root.manager.current = 'main'
    MDLabel:
        text: "Вопрос"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.95, 'center_y': 0.9}
    MDIconButton:
        icon: 'utilits/ntktuf1.png'
        pos_hint: {'center_x': 0.97, 'center_y': 0.95}
        user_font_size: "100sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.96, 'center_y': 0.94}
        user_font_size: "30sp"
        on_press: root.manager.current = 'main'
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.72}
        size_hint: None, None
        size: "300dp", "150dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: 'Что следует делать в момент штурма спецподразделениями?'
            color: 1,1,1,1
            font_style: 'H3'
            font_size:"20sp"
            halign: 'center'
    MDCard: 
        md_bg_color: 0.63, 0, 1, 1
        radius: [20,]
        border_radius: 20
        size_hint: None, None
        size: 1720, 70
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        text: "Не позволять террористам занять место среди заложников"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'correct'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        text: "По возможности взять в руки оружие убитого преступника и помочь спецназу"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        text: "Громко кричать, указывая спецназу на бандитов, чтобы помочь их распознать"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
        
        
        
<TestthtScreen>: 
    name: 'testtht'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/schoolassistaint.png'
        pos_hint: {'center_x': 0.06, 'center_y': 0.9}
        user_font_size: "100sp"
        on_press: root.manager.current = 'main'
    MDLabel:
        text: "Вопрос"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.95, 'center_y': 0.9}
    MDIconButton:
        icon: 'utilits/ntktuf1.png'
        pos_hint: {'center_x': 0.97, 'center_y': 0.95}
        user_font_size: "100sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.96, 'center_y': 0.94}
        user_font_size: "30sp"
        on_press: root.manager.current = 'main'
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.72}
        size_hint: None, None
        size: "300dp", "150dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: 'Укажите ваши действия при применении слезоточивого газа'
            color: 1,1,1,1
            font_style: 'H3'
            font_size:"20sp"
            halign: 'center'
    MDCard: 
        md_bg_color: 0.63, 0, 1, 1
        radius: [20,]
        border_radius: 20
        size_hint: None, None
        size: 1720, 70
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        text: "Будете дышать неглубоко"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        text: "Будете дышать через мокрый платок и часто моргать"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'correct'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        text: "Накроетесь курткой"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'correct'        


<TestotbScreen>: 
    name: 'testotb'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDIconButton:
        icon: 'utilits/schoolassistaint.png'
        pos_hint: {'center_x': 0.07, 'center_y': 0.9}
        user_font_size: "50sp"
        on_press: root.manager.current = 'main'
    MDLabel:
        text: "Вопрос"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        pos_hint: {'center_x': 0.75, 'center_y': 0.9}
    MDIconButton:
        icon: 'utilits/ntktuf1.png'
        pos_hint: {'center_x': 0.97, 'center_y': 0.95}
        user_font_size: "90sp"
        on_press: root.manager.current = 'main'
    MDIconButton:
        icon: 'utilits/icons8-пожары-52 (1) 2.png'
        pos_hint: {'center_x': 0.94, 'center_y': 0.94}
        user_font_size: "25sp"
        on_press: root.manager.current = 'main'
    MDCard:
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.52, 'center_y': 0.72}
        size_hint: None, None
        size: "250dp", "100dp"
        radius: [30, ]
        border_radius: 30
        MDLabel:
            markup: True
            text: 'Что не запрещается в кабинете информатики?'
            color: 1,1,1,1
            font_style: 'H3'
            font_size:"20sp"
            halign: 'center'
    MDCard: 
        md_bg_color: 0.63, 0, 1, 1
        radius: [20,]
        border_radius: 20
        size_hint: None, None
        size: 1720, 70
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        text: "Работать двум ученикам за одним компьютером"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'correct'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        text: "Отключать и подключать устройства к компьютеру"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    MDFillRoundFlatButton:
        md_bg_color: 0.63, 0, 1, 1
        font_size: "15sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        text: "Громко разговаривать, отвлекать других учеников"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        border_radius: [50,]
        radius: 50
        on_press: root.manager.current = 'wrong'
    
<CorrectScreen>: 
    name: 'correct'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDFillRoundFlatIconButton:
        icon: 'utilits/человечек.png'
        text: 'Назад'
        user_font_size : 180
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.1, 'center_y': 0.9}
        on_press: root.manager.current = 'safety'
    MDLabel:
        text: "Всё правильно. Молодец"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        halign: 'center'

<WrongScreen>: 
    name: 'wrong'
    MDBoxLayout:
        md_bg_color: .35, 0, .56, 1
    MDFillRoundFlatIconButton:
        icon: 'utilits/человечек.png'
        text: 'Назад'
        user_font_size : 180
        md_bg_color: 0.63, 0, 1, 1
        pos_hint: {'center_x': 0.1, 'center_y': 0.9}
        on_press: root.manager.current = 'safety'
    MDLabel:
        text: "Неправильно. Попробуй ещё раз"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H3"
        halign: 'center'
'''


class WelcomeScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class LibraryScreen(Screen):
    pass


class TimetableScreen(Screen):
    pass


class NavigationScreen(Screen):
    pass


class SafetyMethodsScreen(Screen):
    pass


class BuffetScreen(Screen):
    pass


class TestScreen(Screen):
    pass


class SafetyTestScreen(Screen):
    pass


class Klassdes(Screen):
    pass

class Klassdesd(Screen):
    pass

class Klassdesg(Screen):
    pass

class Klassdesv(Screen):
    pass

class Klassdesb(Screen):
    pass

class Klassdesa(Screen):
    pass


class Klassodinna(Screen):
    pass

class Klassodinnb(Screen):
    pass

class Klassodinnv(Screen):
    pass

class Klassodinng(Screen):
    pass

class Klassodinnd(Screen):
    pass

class Klassdeve(Screen):
    pass

class Klassdevz(Screen):
    pass

class WrongScreen(Screen):
    pass

class CorrectScreen(Screen):
    pass


class FloorScreen(Screen):
    pass


class TestterScreen(Screen):
    pass


class TesttbScreen(Screen):
    pass


class TestofScreen(Screen):
    pass


class TesttfScreen(Screen):
    pass


class TestthfScreen(Screen):
    pass


class TestotScreen(Screen):
    pass


class TestttScreen(Screen):
    pass


class TestthtScreen(Screen):
    pass


class TestotbScreen(Screen):
    pass



screen_manager = ScreenManager()
screen_manager.add_widget(WelcomeScreen(name='welcome'))
screen_manager.add_widget(MainScreen(name='main'))
screen_manager.add_widget(SettingsScreen(name='settings'))
screen_manager.add_widget(LibraryScreen(name='library'))
screen_manager.add_widget(NavigationScreen(name='navigation'))
screen_manager.add_widget(TimetableScreen(name='timetable'))
screen_manager.add_widget(SafetyMethodsScreen(name='safety'))
screen_manager.add_widget(BuffetScreen(name='buffet'))
screen_manager.add_widget(TestScreen(name='test'))
screen_manager.add_widget(SafetyTestScreen(name='safety_test'))
screen_manager.add_widget(Klassdesd(name='raspisanie'))
screen_manager.add_widget(Klassdesg(name='raspisaniedesg'))
screen_manager.add_widget(Klassdesv(name='raspisaniedesv'))
screen_manager.add_widget(Klassdesb(name='raspisaniedesb'))
screen_manager.add_widget(Klassdesa(name='raspisaniedesa'))
screen_manager.add_widget(Klassodinnd(name='raspisanieodinnd'))
screen_manager.add_widget(Klassodinng(name='raspisanieodinng'))
screen_manager.add_widget(Klassodinnv(name='raspisanieodinnv'))
screen_manager.add_widget(Klassodinnb(name='raspisanieodinnb'))
screen_manager.add_widget(Klassodinna(name='raspisanieodinna'))
screen_manager.add_widget(Klassdeve(name='raspisanieodinna'))
screen_manager.add_widget(Klassdevz(name='raspisanieodinna'))
screen_manager.add_widget(TestterScreen(name='testter'))
screen_manager.add_widget(TesttbScreen(name='testtb'))
screen_manager.add_widget(TestofScreen(name='testof'))
screen_manager.add_widget(TesttfScreen(name='testtf'))
screen_manager.add_widget(TestthfScreen(name='testthf'))
screen_manager.add_widget(TestotScreen(name='testot'))
screen_manager.add_widget(TestttScreen(name='testtt'))
screen_manager.add_widget(TestthtScreen(name='testtht'))
screen_manager.add_widget(TestotbScreen(name='testotb'))

class SchoolAssistantApp(MDApp):
    def build(self):
        self.screen = Builder.load_string(KV)
        return self.screen


SchoolAssistantApp().run()
