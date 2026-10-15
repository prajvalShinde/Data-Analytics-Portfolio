SELECT COUNT(*) AS total_students FROM students;
SELECT course, COUNT(*) AS enrollments FROM enrollments GROUP BY course ORDER BY enrollments DESC;
SELECT s.city, COUNT(e.enrollment_id) AS enrollments FROM students s LEFT JOIN enrollments e ON s.student_id=e.student_id GROUP BY s.city ORDER BY enrollments DESC;
SELECT s.student_id,s.name FROM students s LEFT JOIN enrollments e ON s.student_id=e.student_id WHERE e.enrollment_id IS NULL;
SELECT course, COUNT(*) AS enrollments FROM enrollments GROUP BY course HAVING COUNT(*)>20;
