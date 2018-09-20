# Análise de Logs
Terceiro projeto do curso nanodegree da Udacity de Desenvolvedor Full-stack.
Esta uma ferramenta de relatórios que imprime relatórios (em texto sem formatação) com base nos dados no banco de dados.

(Veja o resultado gerado do programa)[https://raw.githubusercontent.com/giordanna/Analise-Logs/master/relatorio.txt]

### Como instalar
- Este repositório é apenas o conteúdo que deverá ser inserido na pasta compartilhada do vagrant. Siga os passos [desta página](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) para instalar a máquina virtual com as configurações utilizadas;
- Em seguida, baixe o [banco de dados](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip);
- Coloque na pasta vagrant, compartilhada com a máquina virtual;
- Use o comando `psql -d news -f newsdata.sql` abaixo na máquina virtual dentro do diretório compartilhado:
- Agora, clone ou baixe o conteúdo deste repositório no diretório compartilhado.

### Como criar as Views utilizadas
Este projeto utiliza de views que foram criadas no banco de dados e são referenciadas no `relatório.py`. Para o programa funcionar corretamente, estas views devem ser criadas no banco de dados `news`.
1) Para criar a view `artigos_mais_populares`:
```sql
create view artigos_mais_populares as
select articles.title, count(log.path) as views
from log, articles
where log.status = '200 OK' and log.path like concat('%', articles.slug)
group by log.path, articles.title
order by views desc;
```

2) Para criar a view `autores_mais_populares`:
```sql
create view autores_mais_populares as
select authors.name, count(articles.author) as views
from log, articles, authors
where log.status = '200 OK' and log.path like concat('%', articles.slug) and articles.author=authors.id
group by articles.author, authors.name
order by views desc limit 3;
```

3) Para criar a view `dias_com_mais_de_1_por_cento_de_erros`:
```sql
create view dias_com_mais_de_1_por_cento_de_erros as

select * from

(select to_char(ers.data, 'Mon DD, YYYY') as data, ers.erros::decimal / oks.validos * 100 as porcentagem from

(select date(log.time) as data, count(date(log.time)) as erros
from log
where log.status != '200 OK'
group by date(log.time)
order by erros desc ) as ers,

(select date(log.time) as data, count(date(log.time)) as validos
from log where log.status = '200 OK'
group by date(log.time)
order by validos desc ) as oks

where ers.data = oks.data

order by porcentagem desc) as consulta

where porcentagem > 1;
```

Estas queries estão também localizadas no repositório.

### Como executar
No terminal da máquina virtual, execute `python relatorio.py`. Aguarde alguns segundos e o arquivo `relatorio.txt` será atualizado. Caso o arquivo não exista previamente, ele será gerado.

### Dúvidas
 - Caso há alguma dúvida em relação a este repositório, envie para gior.grs@gmail.com