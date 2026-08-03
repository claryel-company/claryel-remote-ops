# CLARYEL RemoteOps — instalação e configuração privada

O RemoteOps gere o seu próprio computador Windows, Ubuntu/Linux ou macOS através do chat de IA que escolher.

## 1. Instalar

- [Instalador Windows](../../installers/install-windows.ps1)
- [Instalador macOS](../../installers/install-macos.sh)
- [Instalador Ubuntu](../../installers/install-ubuntu.sh)

Execute o ficheiro descarregado. O RemoteOps instala-se no seu perfil de utilizador, cria uma área local privada e não desativa a segurança do sistema operativo.

## 2. Criar o seu repositório pessoal Private

Instale o GitHub CLI, execute `gh auth login` e depois o comando apresentado pelo instalador:

```text
remoteops connect --path O-SEU-CAMINHO-PRIVADO --create-private remoteops-meu-computador
```

O repositório é criado na sua conta GitHub com visibilidade `Private`. O RemoteOps não o torna público nem adiciona colaboradores.

Private significa oculto do público. Ainda podem aceder o proprietário, pessoas ou aplicações autorizadas por si e o GitHub como operador do serviço. Proteja a conta com passkey ou autenticação de dois fatores.

Nunca guarde no Git palavras-passe, tokens, chaves, códigos de recuperação, ficheiros pessoais, conversas, registos brutos, bases de dados ou cópias de segurança.

## 3. Verificar a privacidade

```text
remoteops privacy-check --path O-SEU-CAMINHO-PRIVADO
```

Continue apenas quando aparecer `"ok": true`, `"visibility": "PRIVATE"` e nenhuma ocorrência.

## 4. Ligar o ChatGPT

1. Abra **ChatGPT > Definições > Apps > GitHub**.
2. Escolha **Apenas repositórios selecionados**.
3. Selecione apenas `remoteops-meu-computador`.
4. Reveja as permissões antes de aceitar.
5. Reveja **Definições > Controlos de dados > Melhorar o modelo para todos**.
6. Nunca cole segredos ou ficheiros pessoais no chat.

A disponibilidade da app GitHub e a escrita variam conforme o plano e o modo do ChatGPT. Uma ligação só de leitura não pode aplicar alterações.

## Limite de comunicações

O RemoteOps contacta o GitHub apenas ao ligar ou sincronizar o repositório privado, o ChatGPT apenas quando decide usá-lo e as fontes de pacotes apenas para operações aprovadas. Os instaladores não adicionam publicidade nem análise externa.

Guias detalhados: [repositório privado](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [privacidade e rede](../../docs/PRIVACY_AND_NETWORK.md).
