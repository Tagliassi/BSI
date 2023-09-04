// Classe Monstro
export class Monstro {
    constructor(nome, vida, dano) {
        this.nome = nome;
        this.vida = vida;
        this.dano = dano;
        this.atualizarCoracoes();
    }

    apresentar() {
        return `ORA ORA SEU TOLO, ME CHAMO ${this.nome} e sou um MONSTRO HORRÍVELll !!! MUAHUAHAUAHAHA\N vou te comer`;
    }

    gritar(){
        return `AHHHHHRRRRRRRWWWWWWWWWWWWWWWWWWWWW\n\n RHHHHWWWWW`;
    }

    atacar(personagem) {
        personagem.vida -= this.dano;
        this.atualizarCoracoes();
    }
    
    apanhar() {

        this.vida--;
        this.atualizarCoracoes();

        if(this.vida < 1){
            clearTimeout(this.evento);
            alert(`Você derrotou ${this.nome}, agora pode seguir em frente`);
        }
    }
    
    lutar(personagem){
        alert("Lute com o monstro, clicando em atacar");
        this.evento = setTimeout(() => personagem.morrer(this.nome), 5000);
    }

    atualizarCoracoes() {
        const heartsContainer = document.querySelector(".monster-status .hearts");
        const caminhoImagemCoracao = "./../../assets/elementos/hearts.png";

        // Remova todos os corações existentes
        heartsContainer.innerHTML = "";

        // Crie corações com base na vida atual
        for (let i = 0; i < this.vida; i++) {
            const heart = document.createElement("img");
            heart.src = caminhoImagemCoracao;

            heart.classList.add("heart");
            heartsContainer.appendChild(heart);
        }
    }
}