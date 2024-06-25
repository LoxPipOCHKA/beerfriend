CREATE TABLE beer (name Text PRIMARY KEY, 
                   variety integer, 
                   description Text, 
                   fortress numeric (2,1),
                   iconurl Text
	);
        
CREATE TABLE feedback(id INTEGER PRIMARY KEY ,
                     name Text,
                     comment text,
                     nick text,
                     estimation integer,
                     FOREIGN KEY (name) REFERENCES beer (name) ON DELETE  CASCADE
                     );

	create table variety(id integer Primary key,
	variety text
	
	);

insert into variety values(1, 'Светлое'),
(2,'Тёмное'),
(3, 'Стаут'),
(4, 'Портер'),
(5, 'Пшеничное'),
(6, 'Эль'),
(7, 'Крепкое'),
(8, 'Сидорас');

ALTER TABLE beer ADD CONSTRAINT fk_sort_id FOREIGN KEY (variety) REFERENCES variety(id);

SELECT beer.description,
       beer.iconurl,
beer.name,	
       feedback.comment,
	feedback.nick,
	feedback.estimation,
       ROUND((SELECT AVG(feedback.estimation) FROM feedback WHERE feedback.name = ''), 1) AS average_rating
FROM beer
LEFT OUTER JOIN feedback ON beer.name = feedback.name
WHERE  beer.name = '';





