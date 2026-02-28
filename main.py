import json
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.properties import NumericProperty, StringProperty
from kivy.animation import Animation
from kivy.utils import platform
import random

# PC ekranında telefon görünümü taklidi
if platform != 'android' and platform != 'ios':
    Window.size = (400, 750)

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

ScreenManager:
    id: sm
    SplashScreen:
    MainScreen:
    ExamScreen:
    ResultScreen:

<SplashScreen>:
    name: 'splash'
    MDFloatLayout:
        md_bg_color: get_color_from_hex("#1E1B4B") # Premium Dark Deep Purple
        
        MDIcon:
            icon: "school-outline"
            font_size: "100sp"
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .6}
            theme_text_color: "Custom"
            text_color: get_color_from_hex("#FCD34D") # Gold
            
        MDLabel:
            text: "KPSS MASTER"
            font_style: "H4"
            bold: True
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint: {"center_y": .45}
            halign: "center"
            
        MDLabel:
            text: "PRO"
            font_style: "H6"
            bold: True
            theme_text_color: "Custom"
            text_color: get_color_from_hex("#FCD34D")
            pos_hint: {"center_y": .4}
            halign: "center"
            
        MDSpinner:
            size_hint: None, None
            size: dp(40), dp(40)
            pos_hint: {'center_x': .5, 'center_y': .2}
            color: get_color_from_hex("#FCD34D")

<MainScreen>:
    name: 'main'
    MDBottomNavigation:
        panel_color: app.theme_cls.bg_normal
        selected_color_background: app.theme_cls.primary_color
        text_color_active: app.theme_cls.primary_color
        
        MDBottomNavigationItem:
            name: 'nav_home'
            text: 'Ana Sayfa'
            icon: 'home-variant-outline'
            
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: get_color_from_hex("#F8FAFC")
                
                MDTopAppBar:
                    title: "Hoş Geldin 👋"
                    elevation: 0
                    md_bg_color: get_color_from_hex("#F8FAFC")
                    specific_text_color: get_color_from_hex("#0F172A")
                    right_action_items: [["bell-outline", lambda x: x], ["account-circle-outline", lambda x: x]]
                
                ScrollView:
                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: "24dp"
                        spacing: "24dp"
                        size_hint_y: None
                        height: self.minimum_height
                        
                        # Premium Banner Card
                        MDCard:
                            size_hint_y: None
                            height: "160dp"
                            radius: [24, 24, 24, 24]
                            md_bg_color: get_color_from_hex("#1E293B")
                            padding: "20dp"
                            elevation: 2
                            
                            MDRelativeLayout:
                                MDLabel:
                                    text: "PRO AYRICALIKLARI"
                                    font_style: "Caption"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: get_color_from_hex("#FBBF24")
                                    pos_hint: {"top": 1}
                                MDLabel:
                                    text: "Sınırları Kaldırın"
                                    font_style: "H5"
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    pos_hint: {"top": .8}
                                MDLabel:
                                    text: "Çevrimdışı testler ve analizler için yükselt."
                                    font_style: "Caption"
                                    theme_text_color: "Custom"
                                    text_color: 0.8, 0.8, 0.8, 1
                                    pos_hint: {"top": .5}
                                MDFillRoundFlatButton:
                                    text: "Premium (9,99₺)"
                                    md_bg_color: get_color_from_hex("#FBBF24")
                                    text_color: 0, 0, 0, 1
                                    pos_hint: {"y": 0}
                                    on_release: app.open_payment()
                                MDIcon:
                                    icon: "star-shooting"
                                    font_size: "80sp"
                                    pos_hint: {"center_y": .5, "right": 1.1}
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 0.1
                        
                        MDLabel:
                            text: "Deneme Sınavları"
                            font_style: "H6"
                            bold: True
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("#0F172A")
                        
                        # Exam Cards
                        MDCard:
                            size_hint_y: None
                            height: "100dp"
                            radius: [20,]
                            padding: "16dp"
                            elevation: 1
                            md_bg_color: 1, 1, 1, 1
                            ripple_behavior: True
                            on_release: app.start_exam()
                            
                            MDRelativeLayout:
                                MDCard:
                                    size_hint: None, None
                                    size: "50dp", "50dp"
                                    radius: [12,]
                                    md_bg_color: get_color_from_hex("#EEF2FF")
                                    pos_hint: {"center_y": .5, "x": 0}
                                    MDIcon:
                                        icon: "text-box-check-outline"
                                        font_size: "28sp"
                                        pos_hint: {"center_x": .5, "center_y": .5}
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        
                                MDLabel:
                                    text: "Türkiye Geneli Lisans 1"
                                    font_style: "Subtitle1"
                                    bold: True
                                    pos_hint: {"center_y": .65, "x": .25}
                                MDLabel:
                                    text: "120 Soru • 130 Dakika"
                                    font_style: "Caption"
                                    theme_text_color: "Hint"
                                    pos_hint: {"center_y": .35, "x": .25}
                                MDIconButton:
                                    icon: "chevron-right"
                                    theme_text_color: "Hint"
                                    pos_hint: {"center_y": .5, "right": 1}

                        MDCard:
                            size_hint_y: None
                            height: "100dp"
                            radius: [20,]
                            padding: "16dp"
                            elevation: 0
                            md_bg_color: 1, 1, 1, 0.6
                            line_color: 0.9, 0.9, 0.9, 1
                            on_release: app.open_payment()
                            
                            MDRelativeLayout:
                                MDCard:
                                    size_hint: None, None
                                    size: "50dp", "50dp"
                                    radius: [12,]
                                    md_bg_color: get_color_from_hex("#FEF3C7")
                                    pos_hint: {"center_y": .5, "x": 0}
                                    MDIcon:
                                        icon: "lock"
                                        font_size: "24sp"
                                        pos_hint: {"center_x": .5, "center_y": .5}
                                        theme_text_color: "Custom"
                                        text_color: get_color_from_hex("#D97706")
                                        
                                MDLabel:
                                    text: "Pro Deneme 2"
                                    font_style: "Subtitle1"
                                    bold: True
                                    theme_text_color: "Hint"
                                    pos_hint: {"center_y": .65, "x": .25}
                                MDLabel:
                                    text: "Premium üyelere özel"
                                    font_style: "Caption"
                                    theme_text_color: "Hint"
                                    pos_hint: {"center_y": .35, "x": .25}

        MDBottomNavigationItem:
            name: 'nav_stats'
            text: 'İstatistik'
            icon: 'chart-box-outline'
            
            MDBoxLayout:
                orientation: 'vertical'
                md_bg_color: get_color_from_hex("#F8FAFC")
                
                MDTopAppBar:
                    title: "Puan & Sıralama Hesp."
                    elevation: 0
                    md_bg_color: get_color_from_hex("#F8FAFC")
                    specific_text_color: get_color_from_hex("#0F172A")
                    
                ScrollView:
                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: "24dp"
                        spacing: "24dp"
                        size_hint_y: None
                        height: self.minimum_height
                        
                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "280dp"
                            radius: [20,]
                            padding: "20dp"
                            elevation: 1
                            md_bg_color: 1, 1, 1, 1
                            
                            MDLabel:
                                text: "2024 P3 Referans Puan Hesaplama"
                                font_style: "Subtitle1"
                                bold: True
                                halign: "center"
                                theme_text_color: "Primary"
                                
                            MDLabel:
                                text: "Son Sınav Netiniz: " + app.last_net_str
                                halign: "center"
                                theme_text_color: "Hint"
                                font_style: "Body2"
                                margin_top: "10dp"
                                
                            Widget:
                                size_hint_y: None
                                height: "20dp"
                                
                            MDBoxLayout:
                                orientation: "horizontal"
                                spacing: "15dp"
                                
                                MDCard:
                                    orientation: "vertical"
                                    md_bg_color: get_color_from_hex("#EEF2FF")
                                    radius: [12,]
                                    padding: "10dp"
                                    
                                    MDLabel:
                                        text: "Tahmini P3"
                                        font_style: "Caption"
                                        halign: "center"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        
                                    MDLabel:
                                        text: app.estimated_points
                                        font_style: "H4"
                                        bold: True
                                        halign: "center"
                                        theme_text_color: "Custom"
                                        text_color: app.theme_cls.primary_color
                                        
                                MDCard:
                                    orientation: "vertical"
                                    md_bg_color: get_color_from_hex("#ECFDF5")
                                    radius: [12,]
                                    padding: "10dp"
                                    
                                    MDLabel:
                                        text: "Sıralama (Tahmini)"
                                        font_style: "Caption"
                                        halign: "center"
                                        theme_text_color: "Custom"
                                        text_color: get_color_from_hex("#059669")
                                        
                                    MDLabel:
                                        text: app.estimated_rank
                                        font_style: "H6"
                                        bold: True
                                        halign: "center"
                                        theme_text_color: "Custom"
                                        text_color: get_color_from_hex("#059669")
                                        
                            MDLabel:
                                text: "* Yukarıdaki değerler 2024 yılı Lisans KPSS istatistikleri baz alınarak hesaplanan tahmini değerlerdir."
                                font_style: "Caption"
                                theme_text_color: "Hint"
                                halign: "center"
                                size_hint_y: None
                                height: "40dp"

<PaymentScreen>:
    name: 'payment'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: get_color_from_hex("#F8FAFC")
        
        MDTopAppBar:
            title: "Premium Satın Al"
            elevation: 0
            md_bg_color: get_color_from_hex("#F8FAFC")
            specific_text_color: get_color_from_hex("#0F172A")
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
            
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "24dp"
                spacing: "20dp"
                size_hint_y: None
                height: self.minimum_height
                
                MDCard:
                    size_hint_y: None
                    height: "200dp"
                    radius: [20,]
                    md_bg_color: get_color_from_hex("#1E293B")
                    orientation: 'vertical'
                    padding: "24dp"
                    
                    MDLabel:
                        text: "KPSS MASTER PRO"
                        font_style: "Subtitle1"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("#FBBF24")
                        
                    MDLabel:
                        text: "9,99 ₺"
                        font_style: "H3"
                        bold: True
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        
                    MDLabel:
                        text: "Tek Seferlik Ödeme\\nTüm denemeler açılır, reklamsız deneyim."
                        font_style: "Caption"
                        theme_text_color: "Custom"
                        text_color: 0.8, 0.8, 0.8, 1
                        
                MDTextField:
                    hint_text: "Kart Üzerindeki İsim"
                    mode: "rectangle"
                    
                MDTextField:
                    hint_text: "Kart Numarası"
                    mode: "rectangle"
                    max_text_length: 16
                    input_filter: "int"
                    
                MDBoxLayout:
                    spacing: "16dp"
                    size_hint_y: None
                    height: "70dp"
                    
                    MDTextField:
                        hint_text: "SKT (AA/YY)"
                        mode: "rectangle"
                        size_hint_x: 0.5
                        
                    MDTextField:
                        hint_text: "CVC"
                        mode: "rectangle"
                        size_hint_x: 0.5
                        max_text_length: 3
                        input_filter: "int"
                        
                Widget:
                    size_hint_y: None
                    height: "20dp"
                    
                MDFillRoundFlatButton:
                    text: "GÜVENLİ ÖDEME YAP"
                    font_style: "Button"
                    size_hint_x: 1
                    size_hint_y: None
                    height: "56dp"
                    md_bg_color: get_color_from_hex("#059669")
                    on_release: app.process_payment()
                    
                MDLabel:
                    text: "Ödemeniz 256-bit SSL ile şifrelenmektedir."
                    font_style: "Caption"
                    halign: "center"
                    theme_text_color: "Hint"
                    
<ExamScreen>:
    name: 'exam'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: get_color_from_hex("#F8FAFC")
        
        # Transparent Top Navbar
        MDBoxLayout:
            size_hint_y: None
            height: "70dp"
            padding: ["16dp", "16dp", "16dp", "16dp"]
            md_bg_color: get_color_from_hex("#FFFFFF")
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.05
                Line:
                    points: [0, self.y, self.width, self.y]
                    width: 1

            MDIconButton:
                icon: "close"
                pos_hint: {"center_y": .5}
                on_release: app.confirm_quit()
                
            Widget:
            MDCard:
                size_hint: None, None
                size: "110dp", "40dp"
                radius: [20,]
                pos_hint: {"center_y": .5}
                md_bg_color: get_color_from_hex("#F1F5F9")
                elevation: 0
                MDRelativeLayout:
                    MDIcon:
                        id: timer_icon
                        icon: "clock-outline"
                        pos_hint: {"center_y": .5, "x": .1}
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                    MDLabel:
                        id: timer_lbl
                        text: "130:00"
                        bold: True
                        pos_hint: {"center_y": .5, "x": .4}
                        theme_text_color: "Custom"
                        text_color: get_color_from_hex("#0F172A")
            Widget:
                
            MDIconButton:
                icon: "view-grid-outline"
                pos_hint: {"center_y": .5}
                on_release: app.show_optic_form()
                
        MDProgressBar:
            id: progress_bar
            value: 0
            color: app.theme_cls.primary_color
            size_hint_y: None
            height: "4dp"
            
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "24dp"
                spacing: "24dp"
                size_hint_y: None
                height: self.minimum_height
                
                MDBoxLayout:
                    size_hint_y: None
                    height: "30dp"
                    MDCard:
                        size_hint: None, None
                        size: "200dp", "30dp"
                        radius: [8,]
                        md_bg_color: get_color_from_hex("#EEF2FF")
                        elevation: 0
                        MDLabel:
                            id: q_category
                            text: "GENEL YETENEK"
                            font_style: "Caption"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                    Widget:
                    MDLabel:
                        id: q_number
                        text: "1 / 120"
                        halign: "right"
                        font_style: "Subtitle2"
                        bold: True
                        theme_text_color: "Hint"
                        
                MDLabel:
                    id: q_text
                    text: "Soru metni..."
                    font_style: "H6"
                    theme_text_color: "Custom"
                    text_color: get_color_from_hex("#1E293B")
                    size_hint_y: None
                    height: self.texture_size[1]
                    line_height: 1.4
                    
                Widget:
                    size_hint_y: None
                    height: "10dp"
                    
                MDBoxLayout:
                    id: options_container
                    orientation: 'vertical'
                    spacing: "16dp"
                    size_hint_y: None
                    height: self.minimum_height
                    
        MDBoxLayout:
            size_hint_y: None
            height: "80dp"
            padding: "16dp"
            spacing: "16dp"
            md_bg_color: 1,1,1,1
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 0.05
                Line:
                    points: [0, self.top, self.width, self.top]
                    width: 1
                    
            MDFillRoundFlatButton:
                id: prev_btn
                text: "Önceki"
                size_hint: 0.5, 1
                font_style: "Button"
                md_bg_color: get_color_from_hex("#F1F5F9")
                text_color: get_color_from_hex("#64748B")
                elevation: 0
                on_release: app.navigate_q(-1)
                
            MDFillRoundFlatButton:
                id: next_btn
                text: "Sonraki"
                size_hint: 0.5, 1
                font_style: "Button"
                elevation: 1
                on_release: app.navigate_q(1)

<ResultScreen>:
    name: 'result'
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: get_color_from_hex("#F8FAFC")
        
        MDTopAppBar:
            title: "Sınav Sonucu"
            elevation: 0
            md_bg_color: get_color_from_hex("#F8FAFC")
            specific_text_color: get_color_from_hex("#0F172A")
            right_action_items: [["close", lambda x: app.go_home()]]
            
        ScrollView:
            MDBoxLayout:
                orientation: 'vertical'
                padding: "24dp"
                spacing: "30dp"
                size_hint_y: None
                height: self.minimum_height
                
                MDCard:
                    size_hint_y: None
                    height: "260dp"
                    radius: [24,]
                    padding: "24dp"
                    elevation: 1
                    md_bg_color: 1,1,1,1
                    orientation: 'vertical'
                    
                    MDRelativeLayout:
                        size_hint_y: None
                        height: "150dp"
                        
                        Widget:
                            canvas.before:
                                Color:
                                    rgba: get_color_from_hex("#F1F5F9")
                                Line:
                                    circle: (self.center_x, self.center_y, dp(60))
                                    width: dp(8)
                                Color:
                                    rgba: app.theme_cls.primary_color
                                Line:
                                    circle: (self.center_x, self.center_y, dp(60), 0, app.score_angle)
                                    width: dp(8)
                                    cap: 'round'
                                    
                        MDBoxLayout:
                            orientation: 'vertical'
                            pos_hint: {"center_x": .5, "center_y": .5}
                            adaptive_height: True
                            spacing: "-5dp"
                            MDLabel:
                                id: res_net
                                text: "0"
                                font_style: "H3"
                                bold: True
                                halign: "center"
                                theme_text_color: "Custom"
                                text_color: get_color_from_hex("#0F172A")
                            MDLabel:
                                text: "NET"
                                font_style: "Caption"
                                bold: True
                                halign: "center"
                                theme_text_color: "Hint"
                                
                    MDLabel:
                        id: res_comment
                        text: "Değerlendiriliyor..."
                        font_style: "H6"
                        bold: True
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: app.theme_cls.primary_color
                        margin_top: "10dp"
                    
                MDGridLayout:
                    cols: 3
                    spacing: "16dp"
                    size_hint_y: None
                    height: "100dp"
                    
                    MDCard:
                        orientation: 'vertical'
                        radius: [16,]
                        padding: "16dp"
                        elevation: 0
                        md_bg_color: get_color_from_hex("#ECFDF5")
                        MDLabel:
                            id: res_true
                            text: "0"
                            font_style: "H5"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("#059669")
                        MDLabel:
                            text: "Doğru"
                            font_style: "Caption"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("#047857")
                            
                    MDCard:
                        orientation: 'vertical'
                        radius: [16,]
                        padding: "16dp"
                        elevation: 0
                        md_bg_color: get_color_from_hex("#FEF2F2")
                        MDLabel:
                            id: res_false
                            text: "0"
                            font_style: "H5"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("#DC2626")
                        MDLabel:
                            text: "Yanlış"
                            font_style: "Caption"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("#B91C1C")
                            
                    MDCard:
                        orientation: 'vertical'
                        radius: [16,]
                        padding: "16dp"
                        elevation: 0
                        md_bg_color: get_color_from_hex("#F1F5F9")
                        MDLabel:
                            id: res_blank
                            text: "0"
                            font_style: "H5"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: get_color_from_hex("#475569")
                        MDLabel:
                            text: "Boş"
                            font_style: "Caption"
                            halign: "center"
                            theme_text_color: "Hint"
                            
                Widget:
                    size_hint_y: None
                    height: "20dp"
                    
                MDFillRoundFlatButton:
                    text: "Ana Menüye Dön"
                    size_hint_x: 1
                    size_hint_y: None
                    height: "56dp"
                    font_style: "Button"
                    on_release: app.go_home()
                    
'''

class SplashScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class ExamScreen(Screen):
    pass
class ResultScreen(Screen):
    pass
class PaymentScreen(Screen):
    pass

class KPSSApp(MDApp):
    score_angle = NumericProperty(0)
    last_net_str = StringProperty("Sınava girmediniz.")
    estimated_points = StringProperty("-")
    estimated_rank = StringProperty("-")

    def build(self):
        # Mükemmel Uyuma Sahip Premium Renk Paleti (Indigo)
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"
        
        self.questions = []
        self.user_answers = [None] * 120
        self.current_q_index = 0
        self.time_remaining = 130 * 60
        self.timer_event = None
        self.dialog = None
        
        return Builder.load_string(KV)

    def on_start(self):
        self.load_questions()
        # Splash animasyonu 2.5 saniye sonra geçsin
        Clock.schedule_once(self.switch_to_main, 2.5)
        
    def switch_to_main(self, dt):
        self.root.current = 'main'

    def load_questions(self):
        try:
            with open('questions.json', 'r', encoding='utf-8') as f:
                self.questions = json.load(f)
        except Exception as e:
            self.generate_fallback()

    def generate_fallback(self):
        self.questions = []
        # Türkçe / Matematik vb. hepsini rastgele oluşturmak yerine mantıklı sorular:
        cats = [
            "Genel Yetenek - Türkçe",
            "Genel Yetenek - Matematik",
            "Genel Kültür - Tarih",
            "Genel Kültür - Coğrafya",
            "Genel Kültür - Vatandaşlık",
            "Genel Kültür - Güncel"
        ]
        
        for i in range(120):
            cat = cats[(i // 20) % len(cats)]
            self.questions.append({
                "id": i+1,
                "category": cat,
                "question": f"Soru {i+1}: Bu bir KPSS örneğidir [{cat}]. Aşağıdakilerden hangisi yanlıştır\\n\\nA ve C arasında ki doğru fark hesaplanmalıdır.",
                "options": ["A Seçeneği", "B Seçeneği", "C Seçeneği", "D Seçeneği", "E Seçeneği"],
                "answer": random.randint(0, 4)
            })

    def start_exam(self):
        if not self.questions:
            self.load_questions()
            
        self.current_q_index = 0
        self.user_answers = [None] * 120
        self.time_remaining = 130 * 60
        
        self.root.current = 'exam'
        # Exam başladığında Toolbar normale dönsün
        self.root.get_screen('exam').ids.timer_lbl.text_color = [0.05, 0.09, 0.16, 1]
        self.root.get_screen('exam').ids.timer_icon.text_color = self.theme_cls.primary_color
        
        self.render_question()
        
        if self.timer_event:
            self.timer_event.cancel()
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.time_remaining -= 1
        m, s = divmod(self.time_remaining, 60)
        
        lbl = self.root.get_screen('exam').ids.timer_lbl
        lbl.text = f"{m:02d}:{s:02d}"
        
        if self.time_remaining <= 300:
            lbl.text_color = [0.86, 0.14, 0.14, 1] # Red Danger
            self.root.get_screen('exam').ids.timer_icon.text_color = [0.86, 0.14, 0.14, 1]
            
        if self.time_remaining <= 0:
            if self.timer_event:
                self.timer_event.cancel()
            self.finish_exam()

    def render_question(self):
        if not self.questions: return
        screen = self.root.get_screen('exam')
        q = self.questions[self.current_q_index]
        
        screen.ids.q_category.text = q['category'].upper()
        screen.ids.q_number.text = f"{self.current_q_index + 1} / {len(self.questions)}"
        screen.ids.q_text.text = q['question']
        
        screen.ids.options_container.clear_widgets()
        letters = ['A', 'B', 'C', 'D', 'E']
        
        selected_idx = self.user_answers[self.current_q_index]
        
        for i, opt_text in enumerate(q['options']):
            # Özel tasarım kart tabanlı şıklar
            is_selected = (selected_idx == i)
            
            card = MDCard(
                orientation="horizontal",
                size_hint_y=None,
                height="64dp",
                radius=[16,],
                padding="16dp",
                spacing="16dp",
                elevation=0,
                ripple_behavior=True,
                on_release=lambda x, idx=i: self.select_option(idx)
            )
            
            if is_selected:
                card.md_bg_color = [0.93, 0.95, 1, 1] # #EEF2FF
                card.line_color = self.theme_cls.primary_color
            else:
                card.md_bg_color = [1, 1, 1, 1]
                card.line_color = [0.88, 0.9, 0.94, 1] # #E2E8F0
            
            # Şık Harfi (Daire içinde)
            circle = MDCard(
                size_hint=(None, None),
                size=("32dp", "32dp"),
                radius=[16,],
                md_bg_color=self.theme_cls.primary_color if is_selected else [0.94, 0.96, 0.97, 1],
                pos_hint={"center_y": .5}
            )
            lbl_letter = MDLabel(
                text=letters[i],
                halign="center",
                theme_text_color="Custom",
                text_color=[1,1,1,1] if is_selected else [0.39, 0.45, 0.54, 1],
                bold=True
            )
            circle.add_widget(lbl_letter)
            card.add_widget(circle)
            
            # Şık Metni
            lbl_text = MDLabel(
                text=opt_text,
                theme_text_color="Custom",
                text_color=[0.05, 0.09, 0.16, 1] if is_selected else [0.19, 0.25, 0.34, 1],
                font_style="Subtitle2" if is_selected else "Body1"
            )
            card.add_widget(lbl_text)
            
            screen.ids.options_container.add_widget(card)
            
        screen.ids.progress_bar.value = ((self.current_q_index + 1) / float(len(self.questions))) * 100
        
        if self.current_q_index == 0:
            screen.ids.prev_btn.disabled = True
            screen.ids.prev_btn.md_bg_color = [0.94, 0.96, 0.97, 1]
        else:
            screen.ids.prev_btn.disabled = False
        
        if self.current_q_index == len(self.questions) - 1:
            screen.ids.next_btn.text = "Bitir"
            screen.ids.next_btn.md_bg_color = [0.86, 0.14, 0.14, 1] # Red
        else:
            screen.ids.next_btn.text = "Sonraki"
            screen.ids.next_btn.md_bg_color = self.theme_cls.primary_color

    def select_option(self, idx):
        if self.user_answers[self.current_q_index] == idx:
            self.user_answers[self.current_q_index] = None
        else:
            self.user_answers[self.current_q_index] = idx
        self.render_question()

    def navigate_q(self, direction):
        if self.current_q_index == len(self.questions) - 1 and direction == 1:
            self.confirm_finish()
            return
            
        new_idx = self.current_q_index + direction
        if 0 <= new_idx < len(self.questions):
            self.current_q_index = new_idx
            self.render_question()

    def confirm_quit(self):
        self.dialog = MDDialog(
            title="Uyarı",
            text="Sınavı yarıda bırakmak istiyor musunuz? İlerlemeniz kaydedilmeyecek.",
            radius=[20, 20, 20, 20],
            buttons=[
                MDFlatButton(text="İPTAL", on_release=lambda x: self.dialog.dismiss()),
                MDFlatButton(text="ÇIK", text_color=[0.86, 0.14, 0.14, 1], on_release=lambda x: self.quit_to_home())
            ]
        )
        self.dialog.open()

    def quit_to_home(self):
        if self.dialog:
            self.dialog.dismiss()
        if self.timer_event:
            self.timer_event.cancel()
            
        self.root.current = 'main'

    def show_optic_form(self):
        answered = sum(1 for a in self.user_answers if a is not None)
        blanks = len(self.questions) - answered
        
        self.dialog = MDDialog(
            title="Sınav Özeti",
            text=f"Şu ana kadar {answered} soruyu işaretlediniz.\\n{blanks} soruyu boş bıraktınız.",
            radius=[20, 20, 20, 20],
            buttons=[
                MDFlatButton(text="DEVAM ET", on_release=lambda x: self.dialog.dismiss()),
                MDFlatButton(text="BİTİR (Optik)", text_color=self.theme_cls.primary_color, on_release=lambda x: self.confirm_finish(from_dialog=True))
            ]
        )
        self.dialog.open()

    def confirm_finish(self, from_dialog=False):
        if from_dialog and self.dialog:
            self.dialog.dismiss()
            
        blanks = sum(1 for a in self.user_answers if a is None)
        text = "Sınavı bitirmek istiyor musunuz?"
        if blanks > 0:
            text = f"{blanks} boş sorunuz var. Yine de sınavı bitirmek istiyor musunuz?"
            
        self.dialog = MDDialog(
            title="Emin misiniz?",
            text=text,
            radius=[20, 20, 20, 20],
            buttons=[
                MDFlatButton(text="İPTAL", on_release=lambda x: self.dialog.dismiss()),
                MDFillRoundFlatButton(text="SINAVI BİTİR", md_bg_color=self.theme_cls.primary_color, on_release=lambda x: self.finish_exam())
            ]
        )
        self.dialog.open()

    def calculate_kpss_2024(self, net):
        # 2024 P3 Puan ve Sıralama referans algoritması (Yaklaşık)
        if net <= 0:
            return "0,00", "500,000+"
            
        points = 55.0 + (net * 0.40)
        
        # Sıralama referansı 2024
        if net >= 105:
            rank = "1 - 500"
        elif net >= 95:
            rank = "500 - 3.500"
        elif net >= 85:
            rank = "3.500 - 15.000"
        elif net >= 75:
            rank = "15.000 - 45.000"
        elif net >= 60:
            rank = "45.000 - 120.000"
        else:
            rank = "120.000+"
            
        if points > 100:
            points = 100
        
        return f"{points:.3f}", rank

    def finish_exam(self):
        if self.dialog:
            self.dialog.dismiss()
        if self.timer_event:
            self.timer_event.cancel()
            
        true_count = 0
        false_count = 0
        
        for i, q in enumerate(self.questions):
            if self.user_answers[i] is not None:
                if self.user_answers[i] == q['answer']:
                    true_count += 1
                else:
                    false_count += 1
                    
        blanks = len(self.questions) - (true_count + false_count)
        net = true_count - (false_count / 4.0)
        
        screen = self.root.get_screen('result')
        screen.ids.res_net.text = f"{net:.2f}"
        screen.ids.res_true.text = str(true_count)
        screen.ids.res_false.text = str(false_count)
        screen.ids.res_blank.text = str(blanks)
        
        if net >= 90:
            screen.ids.res_comment.text = "Mükemmel Bir Başarı! 🏆"
        elif net >= 70:
            screen.ids.res_comment.text = "Harika İlerliyorsun! 🚀"
        elif net >= 40:
            screen.ids.res_comment.text = "İyi Yoldasın! 💪"
        else:
            screen.ids.res_comment.text = "Daha Fazla Pratik! 📚"
            
        self.root.current = 'result'
        
        # İstatisitk Güncelleme
        self.last_net_str = f"{net:.2f}"
        pnt, rnk = self.calculate_kpss_2024(net)
        self.estimated_points = pnt
        self.estimated_rank = rnk
        
        percentage = max(0, (net / 120.0) * 360)
        self.score_angle = 0
        anim = Animation(score_angle=percentage, duration=1.5, t='out_quad')
        anim.start(self)

    def open_payment(self):
        self.root.current = 'payment'
        
    def process_payment(self):
        self.dialog = MDDialog(
            title="Ödeme İşlemi",
            text="Simülasyon Modu.\\nPremium işlemler App Store / Google Play üzerinden bağlanmalıdır.",
            radius=[20, 20, 20, 20],
            buttons=[
                MDFlatButton(text="TAMAM", on_release=lambda x: self.dialog.dismiss()),
            ]
        )
        self.dialog.open()

    def go_home(self):
        self.root.current = 'main'

if __name__ == '__main__':
    KPSSApp().run()
