create database if not exists next;

use next;

drop table if exists daily_table;
drop table if exists ticker_table;

create table if not exists ticker_table(
	ticker varchar(6) not null,
    year int not null,
    constraint pk_ticker_year primary key(ticker, year)
);

create table if not exists daily_table(
	ticker varchar(6) not null,
	date Date not null,
	open double not null,
    high double not null,
    low double not null,
    close double not null,
    volume bigint unsigned not null,
    constraint pk_ticker_date primary key(ticker, date),
    constraint fk_ticker foreign key(ticker) references ticker_table(ticker) on update cascade on delete cascade
);

select * from `next`.`ticker_table`;
select * from `next`.`daily_table`;
select count(*) from `next`.`daily_table`;

select count(*) from `next`.`daily_table` where ticker="AAPl";