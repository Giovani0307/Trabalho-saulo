from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CadastroApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Rótulo (Label) para o nome
        self.nome_label = Label(text="Nome:", font_size=18)
        layout.add_widget(self.nome_label)

        # Campo de texto para o nome
        self.nome_input = TextInput(hint_text="Digite seu nome", font_size=18, size_hint_y=None, height=40)
        layout.add_widget(self.nome_input)

        # Rótulo (Label) para o email
        self.email_label = Label(text="Email:", font_size=18)
        layout.add_widget(self.email_label)

        # Campo de texto para o email
        self.email_input = TextInput(hint_text="Digite seu email", font_size=18, size_hint_y=None, height=40)
        layout.add_widget(self.email_input)

        # Botão para realizar o cadastro
        self.cadastrar_button = Button(text="Cadastrar", font_size=18, size_hint_y=None, height=50)
        self.cadastrar_button.bind(on_press=self.cadastrar)
        layout.add_widget(self.cadastrar_button)

        # Rótulo para exibir o status do cadastro
        self.resultado_label = Label(text="Informações serão exibidas aqui", font_size=18)
        layout.add_widget(self.resultado_label)

        return layout

    def cadastrar(self, instance):
        # Pega os valores inseridos
        nome = self.nome_input.text
        email = self.email_input.text

        # Valida se os campos estão preenchidos
        if nome and email:
            # Exibe as informações cadastradas
            self.resultado_label.text = f"Cadastrado com sucesso!\nNome: {nome}\nEmail: {email}"
        else:
            # Informa que os campos estão vazios
            self.resultado_label.text = "Por favor, preencha todos os campos."

# Rodar o aplicativo
if __name__ == '__main__':
    CadastroApp().run()
