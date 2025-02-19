-- Creates a trigger that decreases quantity of an item adding a new order
DELIMITER $$

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
    BEGIN
        UPDATE items
        SET items.quantity = items.quantity - NEW.number
        WHERE items.name = NEW.item_name;
    END$$

DELIMITER ;
