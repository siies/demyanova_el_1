select * from products where category = 'Электроника';

select * from products where category = 'Одежда' and name LIKE '%женские';

select * from products where category = 'Продукты'  or category = 'Книги';

select * from products where category != 'Бытовая техника';

select * from products where category in ('Электроника', 'Одежда', 'Книги');

select * from products where (category = 'Электроника' and name LIKE 'Samsung%') 
or category = 'Бытовая техника';

select * from products where (category in ('Электроника', 'Одежда', 'Бытовая техника') 
and id between 1 and 15 and and name not LIKE 'Samsung%') 
or category = 'Книги';
