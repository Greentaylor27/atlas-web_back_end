-- Creating first procedure.
DELIMITER $$
CREATE PROCEDURE Addbonus(
    user_id INT,
    project_name VARCHAR(255),
    score INT
)
    BEGIN
        DECLARE project_id INT;
        SELECT id INTO project_id FROM projects WHERE name = project_name;
        
        IF project_id IS NULL THEN
            INSERT INTO projects (name)
            VALUES (project_name);

            SELECT LAST_INSERT_ID() into project_id
        END IF;

        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, project_id, score);
    END $$
DELIMITER ;

