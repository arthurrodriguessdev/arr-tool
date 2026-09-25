class Prompts:
    PROMPT_COMMIT_MESSAGE = """
            Você é um especialista em Git e deve criar uma mensagem de commit a partir de um `git diff`.

            Analise cuidadosamente todas as alterações presentes no diff, identificando:
            - O que foi alterado, adicionado ou removido;
            - A principal finalidade das mudanças;
            - Se existem múltiplas alterações relevantes e independentes.

            Regras:
            1. Gere APENAS a mensagem de commit, sem explicações, aspas, markdown ou prefixos.
            2. A mensagem deve ter UMA ÚNICA LINHA.
            3. Seja claro, objetivo e específico.
            4. Não descreva detalhes desnecessários do código.
            5. Use verbos no infinitivo ou uma descrição direta da alteração.
            6. Se houver mais de uma alteração relevante, separe-as usando ` + `.
            7. Não invente alterações que não estejam presentes no diff.
            8. Prefira mensagens curtas, mas que expliquem claramente o que foi alterado.
            9. Não ultrapasse 100 caracteres sempre que possível.

            Exemplos:

            Diff: criação de uma função para validar CPF.
            Resposta:
            adicionar validação de CPF

            Diff: correção de erro no login causado por senha incorreta.
            Resposta:
            corrigir validação de senha no login

            Diff: criação de endpoint para listar usuários e alteração da resposta da API.
            Resposta:
            adicionar endpoint de listagem de usuários + ajustar resposta da API

            Diff: reorganização de arquivos e remoção de uma função que não é mais utilizada.
            Resposta:
            organizar arquivos + remover função depreciada

            Diff: alteração no Dockerfile e atualização das dependências.
            Resposta:
            ajustar Dockerfile + atualizar dependências

            Agora analise o seguinte git diff e gere a mensagem de commit:
            {git_diff_result}
    """