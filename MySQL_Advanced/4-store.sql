-- Creates a trigger that decreases quantity of an item adding a new order
DELIMITER $$

CREATE TRIGGER decease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.quantity_ordered
    WHERE item_id = NEW.item_id
END $$

DELIMITER ;
