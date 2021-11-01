INSERT INTO user(name, email, address, countrycode, phone, budget) VALUES
('Shivang Bharadwaj', 'shivang.b@columbia.edu', 'Lexington and Broadway 24, New York, NY, 10025', 1, 7186121279, 400),
('Shreeya Jain', 'shreeya.jain@columbia.edu', '235 W 109th St, New York, NY, 10025', 1, 9175821990, 500),
('Mukta Jain', 'mukta7jain@gmail.com', 'DH 196, Vijay Nagar, India, 452010', 91, 9926034190, 1000),
('Nirmit Deshpande', 'nirmitdeshpande@gmail.com', 'Hiranandani Estate, Mumbai, India, 400607', 91, 8187083457, 300),
('Ian Cross', 'ian408@yahoo.com', '176 Lexington Av, New York, NY, 10016', 1, 9165237890, 1250),
('Nathalie Praus', 'nathpraus@gmail.com', '342 W 39th St, New York, NY, 10018', 1, 7198310912, 600),
('Katherina Scholl', 'katescholl@hotmail.com', 'Zhylianska St, 49, Kyiv, Ukraine, 02000', 380, 2356791900, 850),
('Antonio Russo', 'russo88anton@gmail.com', 'Fu Abbigliamo, 38, Roma, Italy, 00193', 39, 3243189034, 200),
('Yongzhou Lee', 'yonzolin@gmail.com', 'Mei Yi Lin 7h, Shenchou, China, 300718', 86, 5167834602, 900),
('Emilia Brunner', 'embrunnner78@gmail.com', '113 Stollenstrauss, Obervellach West, Austria, 9821', 43, 6641485850, 700),
('Diego Garcia', 'diego2gar@gmail.com', 'Vall De Cortez, Nuevo Leon, Mexico, 02300', 52, 8181341123, 680);

INSERT INTO login VALUES 
(1, 'shivangb', 'Shivang@23'),
(2, 'sj459', 'Shreeya!8181'),
(3, 'muktajain', 'Password*1'),
(4, 'nirmitd', 'JamesBond^007'),
(5, '408ian', 'Myfridge##408'),
(6, 'natpraus', 'nat*56Praus'),
(7, 'katekate', 'school42&3K'),
(8, 'russothe', 'Anton&R&21'),
(9, 'yonzolin', 'Patterni$234512'),
(10, 'brunnerem', 'EmiliaNoon%5633'),
(11, 'gardiego', '15%KeepSand%29');

INSERT INTO fridge(model,uid) VALUES 
	('FRIDG60000', 1),
('FRIDG60000', 2), 
('FRIDG70000', 2), 
('FRIDG70000', 3), 
('FRIDG40000', 4), 
('FRIDG60000', 5), 
('FRIDG50000', 6), 
('FRIDG50000', 7), 
('FRIDG40000', 8), 
('FRIDG50000', 9), 
('FRIDG40000', 10), 
('FRIDG40000', 11), 
('FRIDG80000', 8), 
('FRIDG80000', 7), 
('FRIDG50000', 4), 
('FRIDG90000', 11), 
('FRIDG90000', 6);

INSERT INTO category(name) VALUES ('Dairy'), ('Eggs, Meat & Fish'), ('Fruits'), ('Vegetables'), ('Nuts & Seeds'), ('Bread & Bakery'), ('Frozen Foods'), ('Beverages'), ('Alcohol'), ('Condiments');

INSERT INTO content VALUES
('Milk', 1),
('Cheese', 1),
('Yogurt', 1),
('Butter', 1),
('Whipped Cream', 1);

INSERT INTO content VALUES
('Eggs', 2),
('Chicken', 2),
('Sausage', 2),
('Salmon', 2),
('Bacon', 2);

INSERT INTO content VALUES
('Apple', 3),
('Banana', 3),
('Mango', 3),
('Orange', 3),
('Blackberry', 3),
('Strawberry', 3),
('Blueberry', 3),
('Raspberry', 3),
('Cantaloupe', 3),
('Pineapple', 3),
('Watermelon', 3),
('Grape', 3),
('Pear', 3),
('Apricot', 3),
('Cherry', 3);

INSERT INTO content VALUES
('Yellow Bell Pepper', 4),
('Red Bell Pepper', 4),
('Green Bell Pepper', 4),
('Cucumber', 4),
('Lemon', 4),
('Lime', 4),
('Orange Bell Pepper', 4),
('Asparagus', 4),
('Spinach', 4),
('Tomato', 4),
('Avocado', 4),
('Mushroom', 4),
('Eggplant', 4),
('Red Cabbage', 4),
('Green Cabbage', 4),
('Carrot', 4),
('Yellow Onion', 4),
('Red Onion', 4),
('Potato', 4),
('Romaine Lettuce', 4),
('Scallion', 4),
('Brocolli', 4),
('Pumpkin', 4),
('Kale', 4),
('Butternut Squash', 4);

INSERT INTO content VALUES
('Pistachio', 5),
('Cashew', 5),
('Almond', 5),
('Sunflower Seed', 5),
('Peanut', 5),
('Chestnut', 5),
('Walnut', 5),
('Pecan', 5),
('Macadamia Nut', 5),
('Pumpkin Seed', 5);

INSERT INTO content VALUES
('Bread', 6),
('Bagel', 6), 
('Tortilla', 6),
('Donut', 6),
('Burger Bun', 6),
('Hotdog Bun', 6),
('Cinnamon Roll', 6);

INSERT INTO content VALUES
('Ice Cream', 7),
('Frozen Strawberry', 7),
('Frozen Pineapple', 7),
('Frozen Blueberry', 7),
('Frozen Raspberry', 7),
('Frozen Berry Assorted', 7),
('Frozen Pizza', 7),
('Frozen Pea', 7),
('Frozen Okra', 7),
('Frozen Bean', 7),
('Frozen Waffle', 7),
('Frozen Pancake', 7),
('Frozen Mozzarella Stick', 7),
('Frozen Lasagna', 7);

INSERT INTO content VALUES
('Water', 8),
('Orange Juice', 8),
('Mixed Fruit Juice', 8),
('Pineapple Juice', 8),
('Coca-Cola', 8),
('Diet Coke', 8),
('Diet Pepsi', 8),
('Sprite', 8),
('Mountain Dew', 8),
('Coconut Water', 8),
('Orange Gatorade', 8),
('Blue Gatorade', 8);

INSERT INTO content VALUES
('Beer', 9),
('Seltzer', 9),
('Red Wine', 9),
('White Wine', 9),
('Rose', 9),
('Baileys Irish Cream', 9),
('Champagne', 9);

INSERT INTO content VALUES
('Ketchup', 10),
('Barbecue Sauce', 10),
('Teriyaki Sauce', 10),
('Italian Dressing', 10),
('Ranch Dressing', 10),
('Mayonnaise', 10),
('Yellow Mustard', 10),
('Honey Mustard', 10),
('Soy Sauce', 10),
('Maple Syrup', 10);

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
	(1, 1, 1, 948, 'oz', 5.59, 'Westside Market', NOW()+interval '7 days'),
(1, 2, 1, 6, 'unit', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(1, 3, 1, 245, 'oz', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(1, 4, 1, 4, 'unit', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(1, 5, 2, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(1, 11, 3, 1, 'kg', 8.89, 'Morton Williams', NOW()+interval '14 days'),
(1, 12, 3, 0.5, 'kg', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(1, 20, 3, 1, 'unit', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(1, 22, 3, 1, 'kg', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(1, 61, 6, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(9, 68, 7, 500, 'g', 13.59, 'Morton Williams', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
	(4, 15, 3, 1, 'kg', 5.59, 'H Mart', NOW()+interval '7 days'),
(4, 12, 3, 6, 'unit', 6.99, 'Trader Joes', NOW()+interval '7 days'), 
(4, 32, 4, 1, 'g', 2.99, 'Morton Williams', NOW()+interval '7 days'), 
(4, 34, 4, 2, 'kg', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(4, 44, 4, 1, 'kg', 9.99, 'Trader Joes', NOW()+interval '7 days'), 
(4, 53, 5, 500, 'g', 15.59, 'Morton Williams', NOW()+interval '14 days'),
(4, 45, 4, 0.5, 'kg', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(4, 69, 7, 1, 'unit', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(4, 73, 7, 1, 'unit', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(4, 80, 7, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(4, 81, 7, 500, 'unit', 13.59, 'Morton Williams', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
	(5, 1, 1, 948, 'oz', 5.59, 'Westside Market', NOW()+interval '7 days'),
(5, 2, 1, 6, 'unit', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(5, 3, 1, 245, 'oz', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(5, 4, 1, 4, 'unit', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(5, 5, 2, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(6, 11, 3, 1, 'kg', 8.89, 'Morton Williams', NOW()+interval '14 days'),
(6, 12, 3, 0.5, 'kg', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(6, 20, 3, 1, 'unit', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(6, 22, 3, 1, 'kg', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(7, 61, 6, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(7, 68, 7, 500, 'g', 13.59, 'Morton Williams', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
	(8, 15, 3, 1, 'kg', 5.59, 'H Mart', NOW()+interval '7 days'),
(8, 12, 3, 6, 'unit', 6.99, 'Trader Joes', NOW()+interval '7 days'), 
(8, 32, 4, 1, 'g', 2.99, 'Morton Williams', NOW()+interval '7 days'), 
(8, 34, 4, 2, 'kg', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(8, 44, 4, 1, 'kg', 9.99, 'Trader Joes', NOW()+interval '7 days'), 
(8, 53, 5, 500, 'g', 15.59, 'Morton Williams', NOW()+interval '14 days'),
(9, 45, 4, 0.5, 'kg', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(9, 69, 7, 1, 'unit', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(9, 73, 7, 1, 'unit', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(9, 80, 7, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(9, 81, 7, 500, 'unit', 13.59, 'Morton Williams', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
(10, 74, 8, 1, 'unit', 7.59, 'Trader Joes', NOW()+interval '14 days'), 
(10, 88, 8, 500, 'ml', 11.49, 'Trader Joes', NOW()+interval '14 days'), 
(11, 97, 9, 500, 'ml', 4.49, 'Trader Joes', NOW()+interval '14 days'), 
(12, 96, 9, 500, 'ml', 4.99, 'Trader Joes', NOW()+interval '14 days'), 
(12, 53, 5, 1, 'kg', 5.59, 'H Mart', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
	(11, 1, 1, 948, 'oz', 5.59, 'Westside Market', NOW()+interval '7 days'),
(12, 2, 1, 6, 'unit', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(13, 3, 1, 245, 'oz', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(14, 4, 1, 4, 'unit', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(13, 5, 2, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(13, 11, 3, 1, 'kg', 8.89, 'Morton Williams', NOW()+interval '14 days'),
(14, 12, 3, 0.5, 'kg', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(15, 20, 3, 1, 'unit', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(16, 22, 3, 1, 'kg', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(17, 61, 6, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(18, 68, 7, 500, 'g', 13.59, 'Morton Williams', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
	(10, 15, 3, 1, 'kg', 5.59, 'H Mart', NOW()+interval '7 days'),
(10, 12, 3, 6, 'unit', 6.99, 'Trader Joes', NOW()+interval '7 days'), 
(11, 32, 4, 1, 'g', 2.99, 'Morton Williams', NOW()+interval '7 days'), 
(7, 34, 4, 2, 'kg', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(6, 44, 4, 1, 'kg', 9.99, 'Trader Joes', NOW()+interval '7 days'), 
(6, 53, 5, 500, 'g', 15.59, 'Morton Williams', NOW()+interval '14 days'),
(6, 45, 4, 0.5, 'kg', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(6, 69, 7, 1, 'unit', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(6, 73, 7, 1, 'unit', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(6, 80, 7, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(5, 81, 7, 500, 'unit', 13.59, 'Morton Williams', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
	(15, 1, 1, 948, 'oz', 5.59, 'Westside Market', NOW()+interval '7 days'),
(15, 2, 1, 6, 'unit', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(15, 3, 1, 245, 'oz', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(12, 4, 1, 4, 'unit', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(12, 5, 2, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(12, 11, 3, 1, 'kg', 8.89, 'Morton Williams', NOW()+interval '14 days'),
(12, 12, 3, 0.5, 'kg', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(12, 20, 3, 1, 'unit', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(12, 22, 3, 1, 'kg', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(13, 61, 6, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(13, 68, 7, 500, 'g', 13.59, 'Morton Williams', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
	(13, 15, 3, 1, 'kg', 5.59, 'H Mart', NOW()+interval '7 days'),
(13, 12, 3, 6, 'unit', 6.99, 'Trader Joes', NOW()+interval '7 days'), 
(14, 32, 4, 1, 'g', 2.99, 'Morton Williams', NOW()+interval '7 days'), 
(14, 34, 4, 2, 'kg', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(14, 44, 4, 1, 'kg', 9.99, 'Trader Joes', NOW()+interval '7 days'), 
(15, 53, 5, 500, 'g', 15.59, 'Morton Williams', NOW()+interval '14 days'),
(15, 45, 4, 0.5, 'kg', 2.99, 'Trader Joes', NOW()+interval '7 days'), 
(15, 69, 7, 1, 'unit', 4.99, 'Westside Market', NOW()+interval '7 days'), 
(15, 73, 7, 1, 'unit', 8.89, 'Trader Joes', NOW()+interval '21 days'), 
(15, 80, 7, 1, 'unit', 3.59, 'Morton Williams', NOW()+interval '7 days'), 
(15, 81, 7, 500, 'unit', 13.59, 'Morton Williams', NOW()+interval '14 days');

INSERT INTO stores(fid, conid, catid, amount, unit, price, store, expiry) VALUES 
(16, 74, 8, 1, 'unit', 7.59, 'Trader Joes', NOW()+interval '14 days'), 
(16, 88, 8, 500, 'ml', 11.49, 'Trader Joes', NOW()+interval '14 days'), 
(16, 97, 9, 500, 'ml', 4.49, 'Trader Joes', NOW()+interval '14 days'), 
(16, 96, 9, 500, 'ml', 4.99, 'Trader Joes', NOW()+interval '14 days'), 
(16, 53, 5, 1, 'kg', 5.59, 'H Mart', NOW()+interval '14 days');


INSERT INTO CreateSList(fid, conid, catid) VALUES 
(10, 74, 8), 
(12, 5, 2), 
(13, 15, 2), 
(15, 45, 7), 
(1, 53, 5), 
(7, 68, 7), 
(13, 3, 1), 
(14, 44, 4), 
(1, 68, 3), 
(12, 12, 3), 
(10, 88, 8);


INSERT INTO settings(locid, fid, name, temp) VALUES 
(1, 1, 'left door', 3), 
(2, 1, 'right door', 3), 
(3, 1, 'freezer', -4), 
(4, 1, 'drawer', 1), 
(5, 1, 'top shelf', 3), 
(6, 1, 'middle shelf', 2), 
(7, 1, 'bottom shelf', 3), 
(1, 9, 'left door', 3), 
(2, 9, 'right door', 3), 
(3, 9, 'freezer', -15), 
(4, 9, 'drawer', 1), 
(5, 9, 'top shelf', 2), 
(6, 9, 'middle shelf', 2), 
(7, 9, 'bottom shelf', 3);

INSERT INTO log(fid, message) VALUES 
(1, '948 oz Milk added'),
(1, '245 oz Yogurt added'),
(1, '1 unit Pineapple added'),
(4, '1 kg Blackberry added'),
(4, '2 kg Spinach added'),
(6, '1 kg Apple added'),
(8, '500 gm Almond added'),
(9, '0.5 kg Romaine Lettuce added'),
(13, '500 gm Ice Cream added'),
(15, '1 unit Frozen Mozzarella Stick added'),
(16, '500 ml Red Wine added');
