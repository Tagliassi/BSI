// Define um protocolo Notificavel que obriga a ter uma propriedade 'mensagem' e um método 'enviarNotificacao()'
protocol Notificavel {
    var mensagem: Mensagem { get set } // Mensagem associada à notificação
    func enviarNotificacao() // Método para enviar a notificação
}

// Extensão do protocolo Notificavel com uma implementação padrão do método enviarNotificacao()
extension Notificavel {
    func enviarNotificacao() {
        print("Notificação enviada: \(self.mensagem)")
    }
}

// Estrutura que representa um e-mail como uma notificação
struct Email: Notificavel {
    let enderecoEmail: String // Endereço de e-mail do destinatário
    var mensagem: Mensagem // Mensagem da notificação

    init(enderecoEmail: String, mensagem: String) {
        self.enderecoEmail = enderecoEmail
        self.mensagem = Mensagem(tipo: TipoMensagem.lembrete, conteudo: mensagem)
    }

    // Implementação personalizada do método enviarNotificacao()
    func enviarNotificacao() {
        print("Enviando e-mail para \(self.enderecoEmail) \n\(self.mensagem.conteudo)")
    }
}

// Estrutura que representa um SMS como uma notificação
struct Sms: Notificavel {
    let numeroTelefone: String // Número de telefone do destinatário
    var mensagem: Mensagem // Mensagem da notificação

    init(numeroTelefone: String, mensagem: String) {
        self.numeroTelefone = numeroTelefone
        self.mensagem = Mensagem(tipo: TipoMensagem.lembrete, conteudo: mensagem)
    }

    // Implementação personalizada do método enviarNotificacao()
    func enviarNotificacao() {
        print("Enviando SMS para \(numeroTelefone) \n\(self.mensagem.conteudo)")
    }
}

// Estrutura que representa uma notificação push
struct PushNotification: Notificavel {
    let tokenDispositivo: String // Token do dispositivo que receberá a notificação
    var mensagem: Mensagem // Mensagem da notificação

    init(tokenDispositivo: String, mensagem: String) {
        self.tokenDispositivo = tokenDispositivo
        self.mensagem = Mensagem(tipo: TipoMensagem.lembrete, conteudo: mensagem)
    }

    // Implementação personalizada do método enviarNotificacao()
    func enviarNotificacao() {
        print("Mostrando notificação no dispositivo \(tokenDispositivo) \n\(self.mensagem.conteudo)")
    }
}

// Array que contém diferentes tipos de notificações
let array: [Notificavel] = [
    Email(enderecoEmail: "1@example.com", mensagem: "Email Legal"),
    Sms(numeroTelefone: "992029191", mensagem: "Sms Legal"),
    PushNotification(tokenDispositivo: "1102", mensagem: "Notificação Legal")
]

// Percorre o array e envia cada notificação
for notificavel in array {
    notificavel.enviarNotificacao()
}

// Enumeração para definir os tipos de mensagens possíveis
enum TipoMensagem {
    case promocao, lembrete, alerta
}

// Estrutura que representa uma mensagem, contendo um tipo e o conteúdo da mensagem
struct Mensagem {
    var tipo: TipoMensagem // Tipo da mensagem
    var conteudo: String // Conteúdo da mensagem

    init(tipo: TipoMensagem, conteudo: String) {
        self.tipo = tipo
        self.conteudo = conteudo
    }
}

// Integrantes da Equipe:

// André Alija Ramos Agostini
// Rafael Tagliaferro Galafassi