--SELECT ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS id,
--      Rate, PayFrequency, ModifiedDate
--INTO Test_Table

--FROM HumanResources.EmployeePayHistory;
--SELECT * FROM Test_Table;

--SELECT TOP 100 * FROM Test_Table
--ORDER BY id DESC;

/*
INSERT INTO Test_Table (Rate, PayFrequency, ModifiedDate)
VALUES
    (15.50, 1, '2023-10-26'),
    (18.75, 1, '2023-10-25'),
    (20.00, 2, '2023-10-24'),
    (22.50, 1, '2023-10-23'),
    (25.00, 2, '2023-10-22'),
    (30.00, 1, '2023-10-21'),
    (17.25, 2, '2023-10-20'),
    (19.00, 1, '2023-10-19'),
    (21.75, 1, '2023-10-18'),
    (24.50, 1, '2023-10-17');
*/

--SELECT TOP 10* FROM Test_Table
--ORDER BY id DESC;

--UPDATE Test_Table
--SET Rate = Rate * 1.5  -- Increase the rate by 10%
--WHERE ID BETWEEN 60 AND 70;

--SELECT ID, Rate, PayFrequency, ModifiedDate
--FROM Test_Table
--WHERE ID BETWEEN 60 AND 70;

DELETE FROM Test_Table
WHERE ID IN (61, 63, 65, 67);

SELECT ID, Rate, PayFrequency, ModifiedDate
FROM Test_Table
WHERE ID BETWEEN 60 AND 70;
