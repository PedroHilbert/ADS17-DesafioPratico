
create database controleprojetos;
use controleprojetos;

create table if not exists projetos(
	idProjeto int primary key not null auto_increment,
    nome_projeto varchar(35) not null,
    localizacao varchar(60) null,
    escopo varchar(60) null,
    cliente varchar(40) not null,
    data_inicio datetime null
);

-- drop schema controleprojetos;