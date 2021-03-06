from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.picker import MDDatePicker
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import IRightBodyTouch
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivy.uix.widget import Widget
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import os


############IMPORT ARQUIVOS LOCAIS############



##################TELAS APP####################
class WelcomeScreen(Screen):
    pass
class UsernameScreen(Screen):
    pass
class DOB(Screen):
    pass

class Screen1(Screen):      #####CHECKLISTS######
    pass
class Screen2(Screen):      #####MINHAS CHECKLISTS#####
    pass
class Screen3(Screen):     #####CHECKLIST SELECIONADA#####
    pass

class Screen5(Screen):
    pass

class CreateCheckList(ThreeLineIconListItem):
    pass

class ChecklistName(Screen):     #####NOME CHECKLIST#####
    pass

class ChecklistItem1(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem2(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem3(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem4(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem5(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem6(Screen):     #####ITEM 1 NOVA LV#####
    pass

class ChecklistItem7(Screen):     #####ITEM 1 NOVA LV#####
    pass
class ChecklistItem8(Screen):     #####ITEM 1 NOVA LV#####
    pass
class ChecklistItem9(Screen):     #####ITEM 1 NOVA LV#####
    pass


class Profile(Screen):     #####PERFIL#####
    pass


#######INTEGRANDO TELAS NO GERENCIADOR DE SCREEN########
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'welcomescreen'))
sm.add_widget(UsernameScreen(name = 'usernamescreen'))
sm.add_widget(DOB(name = 'dob'))

sm.add_widget(Screen1(name = 'screen1'))
sm.add_widget(Screen2(name = 'screen2'))
sm.add_widget(Screen3(name = 'screen3'))

sm.add_widget(Screen5(name = 'screen5'))
sm.add_widget(ChecklistName(name = 'checklistName'))
sm.add_widget(ChecklistItem1(name = 'checklistItem1'))
sm.add_widget(ChecklistItem2(name = 'checklistItem2'))
sm.add_widget(ChecklistItem3(name = 'checklistItem3'))
sm.add_widget(ChecklistItem4(name = 'checklistItem4'))
sm.add_widget(ChecklistItem5(name = 'checklistItem5'))
sm.add_widget(ChecklistItem6(name = 'checklistItem6'))
sm.add_widget(ChecklistItem7(name = 'checklistItem7'))
sm.add_widget(ChecklistItem8(name = 'checklistItem8'))
sm.add_widget(ChecklistItem9(name = 'checklistItem9'))

sm.add_widget(Profile(name = 'profile'))


############MAQUINARIO APP########################
class PawareApp(MDApp):

    def enable_items_inputs(self):

        ##Item 1
        if self.strng.get_screen('checklistItem1').ids.radio_item1_nc.active == True:
            self.strng.get_screen(f'checklistItem1').ids.acao_item1.disabled = False
            self.strng.get_screen(f'checklistItem1').ids.responsavel_item1.disabled = False
            self.strng.get_screen(f'checklistItem1').ids.prazo_item1.disabled = False

        else:
            self.strng.get_screen(f'checklistItem1').ids.acao_item1.disabled = True
            self.strng.get_screen(f'checklistItem1').ids.responsavel_item1.disabled = True
            self.strng.get_screen(f'checklistItem1').ids.prazo_item1.disabled = True


        ##Item 2
        if self.strng.get_screen('checklistItem2').ids.radio_item2_nc.active == True:
            self.strng.get_screen(f'checklistItem2').ids.acao_item2.disabled = False
            self.strng.get_screen(f'checklistItem2').ids.responsavel_item2.disabled = False
            self.strng.get_screen(f'checklistItem2').ids.prazo_item2.disabled = False

        else:
            self.strng.get_screen(f'checklistItem2').ids.acao_item2.disabled = True
            self.strng.get_screen(f'checklistItem2').ids.responsavel_item2.disabled = True
            self.strng.get_screen(f'checklistItem2').ids.prazo_item2.disabled = True


        ##Item 3
        if self.strng.get_screen('checklistItem3').ids.radio_item3_nc.active == True:
            self.strng.get_screen(f'checklistItem3').ids.acao_item3.disabled = False
            self.strng.get_screen(f'checklistItem3').ids.responsavel_item3.disabled = False
            self.strng.get_screen(f'checklistItem3').ids.prazo_item3.disabled = False

        else:
            self.strng.get_screen(f'checklistItem3').ids.acao_item3.disabled = True
            self.strng.get_screen(f'checklistItem3').ids.responsavel_item3.disabled = True
            self.strng.get_screen(f'checklistItem3').ids.prazo_item3.disabled = True

        ##Item 4
        if self.strng.get_screen('checklistItem4').ids.radio_item4_nc.active == True:
            self.strng.get_screen(f'checklistItem4').ids.acao_item4.disabled = False
            self.strng.get_screen(f'checklistItem4').ids.responsavel_item4.disabled = False
            self.strng.get_screen(f'checklistItem4').ids.prazo_item4.disabled = False

        else:
            self.strng.get_screen(f'checklistItem4').ids.acao_item4.disabled = True
            self.strng.get_screen(f'checklistItem4').ids.responsavel_item4.disabled = True
            self.strng.get_screen(f'checklistItem4').ids.prazo_item4.disabled = True

        ##Item 5
        if self.strng.get_screen('checklistItem5').ids.radio_item5_nc.active == True:
            self.strng.get_screen(f'checklistItem5').ids.acao_item5.disabled = False
            self.strng.get_screen(f'checklistItem5').ids.responsavel_item5.disabled = False
            self.strng.get_screen(f'checklistItem5').ids.prazo_item5.disabled = False

        else:
            self.strng.get_screen(f'checklistItem5').ids.acao_item5.disabled = True
            self.strng.get_screen(f'checklistItem5').ids.responsavel_item5.disabled = True
            self.strng.get_screen(f'checklistItem5').ids.prazo_item5.disabled = True

        ##Item 6
        if self.strng.get_screen('checklistItem6').ids.radio_item6_nc.active == True:
            self.strng.get_screen(f'checklistItem6').ids.acao_item6.disabled = False
            self.strng.get_screen(f'checklistItem6').ids.responsavel_item6.disabled = False
            self.strng.get_screen(f'checklistItem6').ids.prazo_item6.disabled = False

        else:
            self.strng.get_screen(f'checklistItem6').ids.acao_item6.disabled = True
            self.strng.get_screen(f'checklistItem6').ids.responsavel_item6.disabled = True
            self.strng.get_screen(f'checklistItem6').ids.prazo_item6.disabled = True

        ##Item 7
        if self.strng.get_screen('checklistItem7').ids.radio_item7_nc.active == True:
            self.strng.get_screen(f'checklistItem7').ids.acao_item7.disabled = False
            self.strng.get_screen(f'checklistItem7').ids.responsavel_item7.disabled = False
            self.strng.get_screen(f'checklistItem7').ids.prazo_item7.disabled = False

        else:
            self.strng.get_screen(f'checklistItem7').ids.acao_item7.disabled = True
            self.strng.get_screen(f'checklistItem7').ids.responsavel_item7.disabled = True
            self.strng.get_screen(f'checklistItem7').ids.prazo_item7.disabled = True

        ##Item 8
        if self.strng.get_screen('checklistItem8').ids.radio_item8_nc.active == True:
            self.strng.get_screen(f'checklistItem8').ids.acao_item8.disabled = False
            self.strng.get_screen(f'checklistItem8').ids.responsavel_item8.disabled = False
            self.strng.get_screen(f'checklistItem8').ids.prazo_item8.disabled = False

        else:
            self.strng.get_screen(f'checklistItem8').ids.acao_item8.disabled = True
            self.strng.get_screen(f'checklistItem8').ids.responsavel_item8.disabled = True
            self.strng.get_screen(f'checklistItem8').ids.prazo_item8.disabled = True

        ##Item 9
        if self.strng.get_screen('checklistItem9').ids.radio_item9_nc.active == True:
            self.strng.get_screen(f'checklistItem9').ids.acao_item9.disabled = False
            self.strng.get_screen(f'checklistItem9').ids.responsavel_item9.disabled = False
            self.strng.get_screen(f'checklistItem9').ids.prazo_item9.disabled = False

        else:
            self.strng.get_screen(f'checklistItem9').ids.acao_item9.disabled = True
            self.strng.get_screen(f'checklistItem9').ids.responsavel_item9.disabled = True
            self.strng.get_screen(f'checklistItem9').ids.prazo_item9.disabled = True

    def check_lv_items(self):

        #Item 1
        if self.strng.get_screen('checklistItem1').ids.radio_item1_nc.active == True and self.strng.get_screen(
                f'checklistItem1').ids.acao_item1.text.split() != [] and self.strng.get_screen(
                f'checklistItem1').ids.responsavel_item1.text.split() != [] and self.strng.get_screen(
                f'checklistItem1').ids.prazo_item1.text.split() != []:
            self.strng.get_screen(f'checklistItem1').ids.next_button1.disabled = False

        # Item 2
        if self.strng.get_screen('checklistItem2').ids.radio_item2_nc.active == True and self.strng.get_screen(
                f'checklistItem2').ids.acao_item2.text.split() != [] and self.strng.get_screen(
                f'checklistItem2').ids.responsavel_item2.text.split() != [] and self.strng.get_screen(
                f'checklistItem2').ids.prazo_item2.text.split() != []:
            self.strng.get_screen(f'checklistItem2').ids.next_button2.disabled = False

        # Item 3
        if self.strng.get_screen('checklistItem3').ids.radio_item3_nc.active == True and self.strng.get_screen(
                f'checklistItem3').ids.acao_item3.text.split() != [] and self.strng.get_screen(
                f'checklistItem3').ids.responsavel_item3.text.split() != [] and self.strng.get_screen(
                f'checklistItem3').ids.prazo_item3.text.split() != []:
            self.strng.get_screen(f'checklistItem3').ids.next_button3.disabled = False

        # Item 4
        if self.strng.get_screen('checklistItem4').ids.radio_item4_nc.active == True and self.strng.get_screen(
                f'checklistItem4').ids.acao_item4.text.split() != [] and self.strng.get_screen(
                f'checklistItem4').ids.responsavel_item4.text.split() != [] and self.strng.get_screen(
                f'checklistItem4').ids.prazo_item4.text.split() != []:
            self.strng.get_screen(f'checklistItem4').ids.next_button4.disabled = False

        # Item 5
        if self.strng.get_screen('checklistItem5').ids.radio_item5_nc.active == True and self.strng.get_screen(
                f'checklistItem5').ids.acao_item5.text.split() != [] and self.strng.get_screen(
                f'checklistItem5').ids.responsavel_item5.text.split() != [] and self.strng.get_screen(
                f'checklistItem5').ids.prazo_item5.text.split() != []:
            self.strng.get_screen(f'checklistItem5').ids.next_button5.disabled = False

        # Item 6
        if self.strng.get_screen('checklistItem6').ids.radio_item6_nc.active == True and self.strng.get_screen(
                f'checklistItem6').ids.acao_item6.text.split() != [] and self.strng.get_screen(
                f'checklistItem6').ids.responsavel_item6.text.split() != [] and self.strng.get_screen(
                f'checklistItem6').ids.prazo_item6.text.split() != []:
            self.strng.get_screen(f'checklistItem6').ids.next_button6.disabled = False

        # Item 7
        if self.strng.get_screen('checklistItem7').ids.radio_item7_nc.active == True and self.strng.get_screen(
                f'checklistItem7').ids.acao_item7.text.split() != [] and self.strng.get_screen(
                f'checklistItem7').ids.responsavel_item7.text.split() != [] and self.strng.get_screen(
                f'checklistItem7').ids.prazo_item7.text.split() != []:
            self.strng.get_screen(f'checklistItem7').ids.next_button7.disabled = False

        # Item 8
        if self.strng.get_screen('checklistItem8').ids.radio_item8_nc.active == True and self.strng.get_screen(
                f'checklistItem8').ids.acao_item8.text.split() != [] and self.strng.get_screen(
            f'checklistItem8').ids.responsavel_item8.text.split() != [] and self.strng.get_screen(
            f'checklistItem8').ids.prazo_item8.text.split() != []:
            self.strng.get_screen(f'checklistItem8').ids.next_button8.disabled = False

        # Item 9
        if self.strng.get_screen('checklistItem9').ids.radio_item9_nc.active == True and self.strng.get_screen(
                f'checklistItem9').ids.acao_item9.text.split() != [] and self.strng.get_screen(
            f'checklistItem9').ids.responsavel_item9.text.split() != [] and self.strng.get_screen(
            f'checklistItem9').ids.prazo_item9.text.split() != []:
            self.strng.get_screen(f'checklistItem9').ids.next_button9.disabled = False




    ##################CONFIRMAÇAO DE SAIDA FUNÇAO################
    dialog = None
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(

                title="Você deseja mesmo sair ?",

                size_hint= (0.7,0.1),
                text="Você deseja mesmo sair ?",
                buttons=[
                    MDFlatButton(
                        text="Sim", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue_app
                    ),
                    MDFlatButton(
                        text="Não", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue
                    ),
                ],
            )
        self.dialog.open()  
    ####################CONFIRMAR EXCLUIR CHECKLIST######################
    def show_alert__delete_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                size_hint= (0.7,0.1),
                title="Você deseja mesmo excluir ?",
                buttons=[
                    MDFlatButton(
                        text="Sim", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue_excluir
                    ),
                    MDFlatButton(
                        text="Não", text_color=self.theme_cls.primary_color, on_release=self.close_username_dialogue
                    ),
                ],
            )
        self.dialog.open()  

    ################CONFIG DA TELA DA CHECKLIST#################
    def save_in_data(self):
        name =   self.strng.get_screen('screen3').ids.profile_name_input.disabled = False
        data = self.strng.get_screen('screen3').ids.profile_data_input.disabled = False
        responsavel = self.strng.get_screen('screen3').ids.profile_responsavel_input.disabled = False
        acao = self.strng.get_screen('screen3').ids.profile_acao_input.disabled = False
        responsavel_realizar = self.strng.get_screen('screen3').ids.profile_responsavel_realizar_input.disabled = False
        prazo = self.strng.get_screen('screen3').ids.profile_prazo_input.disabled = False
        status  = self.strng.get_screen('screen3').ids.profile_status_input.disabled = False
 
        self.email_text = self.strng.get_screen('dob').ids.email_text_fied.text
        self.store = JsonStore("dataChecklist.json")
        self.store.put('UserInfo',name = name, data= data, responsavel= responsavel, acao= acao, reponsavel_relizar= responsavel_realizar, prazo= prazo, status= status)



    def enable_checklist_inputs(self):
        if self.strng.get_screen('screen3').ids.profile_name_input.disabled == True:

            self.strng.get_screen('screen3').ids.profile_name_input.disabled = False
            
            self.strng.get_screen('screen3').ids.profile_data_input.disabled = False


            self.strng.get_screen('screen3').ids.profile_responsavel_input.disabled = False


            self.strng.get_screen('screen3').ids.profile_acao_input.disabled = False
            self.strng.get_screen('screen3').ids.profile_acao_input.disabled = False
            
            self.strng.get_screen('screen3').ids.profile_responsavel_realizar_input.disabled = False
            self.strng.get_screen('screen3').ids.profile_responsavel_realizar_input.disabled = False

            self.strng.get_screen('screen3').ids.profile_prazo_input.disabled = False
            self.strng.get_screen('screen3').ids.profile_prazo_input.disabled = False

            self.strng.get_screen('screen3').ids.profile_status_input.disabled = False
            self.strng.get_screen('screen3').ids.profile_status_input.disabled = False

            self.strng.get_screen('screen3').ids.save_checklist_button.disabled = False
            self.strng.get_screen('screen3').ids.delete_checklist_button.disabled = False

        else:
            self.strng.get_screen('screen3').ids.profile_name_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_data_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_responsavel_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_acao_input.disabled = True
            self.strng.get_screen('screen3').ids.profile_acao_input.disabled = True
            
            self.strng.get_screen('screen3').ids.profile_responsavel_realizar_input.disabled = True
            self.strng.get_screen('screen3').ids.profile_responsavel_realizar_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_prazo_input.disabled = True
            self.strng.get_screen('screen3').ids.profile_prazo_input.disabled = True

            self.strng.get_screen('screen3').ids.profile_status_input.disabled = True
            self.strng.get_screen('screen3').ids.profile_status_input.disabled = True

            self.strng.get_screen('screen3').ids.save_checklist_button.disabled = True
            self.strng.get_screen('screen3').ids.delete_checklist_button.disabled = True
    #######################CONFIG DA TELA MEU PERFIL################
    def enable_profile_inputs(self):
        if self.strng.get_screen('profile').ids.profile_email_input.disabled == True:

            self.strng.get_screen('profile').ids.profile_email_input.disabled = False
            self.strng.get_screen('profile').ids.profile_email_input.disabled = False

            self.strng.get_screen('profile').ids.profile_name_input.disabled = False
            self.strng.get_screen('profile').ids.profile_name_input.disabled = False

            self.strng.get_screen('profile').ids.save_profile_button.disabled = False

        else:
            self.strng.get_screen('profile').ids.profile_email_input.disabled = True
            self.strng.get_screen('profile').ids.profile_email_input.disabled = True

            self.strng.get_screen('profile').ids.profile_name_input.disabled = True
            self.strng.get_screen('profile').ids.profile_name_input.disabled = True

            self.strng.get_screen('profile').ids.save_profile_button.disabled = True

    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''

    def show_date_picker(self):
        date_dialog = MDDatePicker(callback=self.get_date)
        date_dialog.open()

    def build(self):
        self.strng = Builder.load_file('conteudos.kv') #####CARREGANDO KV DAS TELA####
        return self.strng

    ###############DETALHES DO PERFIL ##############
    try:
        store = JsonStore("userProfile.json")
        nome_perfil = store.get('UserInfo')['name']
        email_perfil = store.get('UserInfo')['email']
    except:
        nome_perfil = "Usuário desconhecido"
        email_perfil = "Email não cadastrado"

    try:
        store = JsonStore("dataChecklist.json")
        list_name = store.get('UserInfo')['name']
        criado_em = store.get('UserInfo')['data']
        criado_por = store.get('UserInfo')['responsavel']
        reponsavel_relizar = store.get('UserInfo')['reponsavel_relizar']
        acao = store.get('UserInfo')['acao']
        prazo = store.get('UserInfo')['prazo']
        status = store.get('UserInfo')['status']
    except:
        pass
        

    #####INICIO DO APP CARREGANDO PERFIL E CADASTRO####
    def on_start(self):             
        self.store = JsonStore("userProfile.json")
        try:
            if self.store.get('UserInfo')['name'] != "":
                self.load_checklists_screen_main()
                self.strng.get_screen('screen1').manager.current = 'screen1'
                
        except KeyError:
            self.strng.get_screen('welcomescreen').manager.current = 'welcomescreen'   

    #########PREENCHIMENTO NOME OBRIGATORIO FUNCAO############
    def check_username(self):
        self.username_text = self.strng.get_screen('usernamescreen').ids.username_text_fied.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.username_text.split() == []:
                cancel_btn_username_dialogue = MDFlatButton(text='OK',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Nome inválido',text = "Por favor preencha um nome válido",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()

        else:
            self.strng.get_screen('usernamescreen').ids.disabled_button.disabled = False

    #################BLOCO DE AVISO NOME INVALIDO##################
    def close_username_dialogue(self,obj):
        self.dialog.dismiss()

    def close_username_dialogue_app(self,obj):
        quit()
    #####################BLOCO DE AVISO ECLUIR CHECKLIST##############
    def close_username_dialogue_excluir(self, obj):
        os. remove("dataChecklist.json") 
        self.dialog.dismiss()

        
    
    def get_email(self):
        self.email_text = self.strng.get_screen('dob').ids.email_text_fied.text
        username_check_false = True
        try:
            int(self.username_text)
        except:
            username_check_false = False
        if username_check_false or self.email_text.split() == []:
                cancel_btn_username_dialogue = MDFlatButton(text='OK',on_release = self.close_username_dialogue)
                self.dialog = MDDialog(title = 'Email inválido',text = "Por favor preencha um email válido",size_hint = (0.7,0.2),buttons = [cancel_btn_username_dialogue])
                self.dialog.open()

        else:
            self.strng.get_screen('dob').ids.disabled_button.disabled = False

        ###############SALVANDO EM UM ARQUIVO OS DADOS LOGIN#################
        self.store.put('UserInfo',name = self.username_text, email = self.email_text)
        
        
        ######BUSCANDO NO BANCO AS CHECKLIST############
    def load_checklists_screen_main(self):
        store = JsonStore("dataChecklist.json")
        self.list_name = store.get('UserInfo')['name']
        criado_por = store.get('UserInfo')['data']
        criado_em = store.get('UserInfo')['responsavel']
        
        self.list_name = ThreeLineIconListItem(
        text=self.list_name,
        secondary_text='Responsável: ' + criado_por,
        tertiary_text='Data de emissão: ' + criado_em, on_release=self.change_screen)
        self.list_name.add_widget(IconLeftWidget(icon='check-box-outline'))
        self.strng.get_screen('screen2').ids.my_checklists.add_widget(self.list_name)
        self.strng.get_screen('screen1').manager.current = 'screen1'

        
    def remove_checklist(self):
        self.strng.get_screen('screen2').ids.my_checklists.remove_widget(self.list_name)
        print(self.list_name)
    

    ############AO SELECIONAR UMA CHECKLIST MUDANDO DE TELA##########
    def change_screen(self, ThreeLineIconListItem):
        self.strng.get_screen('screen3').manager.current = 'screen3'

    ###############MUDANDO A TELA PARA INICIAR A VERIFICACAO###########
    def start_checklist(self):
        self.strng.get_screen('screen5').manager.current = 'screen5'
       
    class ContentNavigationDrawer(BoxLayout):  #######PERFIL########
        pass

    class DrawerList(ThemableBehavior, MDList): ######lISTAS DE AÇÕES DO PERFIL######
        pass

    


PawareApp().run()