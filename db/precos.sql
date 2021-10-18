select moedas.nome as moeda, precos.dia as dia, 
precos.preco as preco from moedas, precos
where moedas.id = precos.moeda
order by moeda asc;


