-- Creates a trigger to update email ONLY if it has been updated.
DELIMITER $$
CREATE TRIGGER update_email
BEFORE UPDATE ON users
FOR EACH ROW
    BEGIN
        IF NEW.email <> OLD.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END$$
DELIMITER ;
