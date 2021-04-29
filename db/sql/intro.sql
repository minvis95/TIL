-- DDL
--데이터 조회
-- SELECT 컬럼명 FROM 테이블명;
SELECT * FROM examples;

-- 테이블 생성
CREATE TABLE classmates(
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INT,
  address TEXT
);

-- 테이블 삭제
DROP TABLE classmates;

-- 테이블명 변경
-- ALTER
ALTER TABLE articles
RENAME TO news;

-- 컬첨 추가
ALTER TABLE news
ADD COLUMN created_at TEXT;

ALTER TABLE news
ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;

-- DML(Data Manipulation Language)
-- 데이터 추가
INSERT INTO classmates(name,age)
VALUES('홍길동',23);
--모든 열에 데이터를 넣을 땐 컬럼 생략 가능
INSERT INTO classmates
VALUES('홍길동',30,'서울');


-- PRIMARY KEY를 지정하지 않으면 rowid가 생성된다.
SELECT rowid, * FROM classmates;
SELECT rowid, name FROM classmates;
-- LIMIT : 몇 개 갖고 올건지
SELECT rowid, name FROM classmates LIMIT 1;
-- OFFSET : 어디서 부터 몇개 가지고 올지
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
-- WHERE : 조건
SELECT rowid, name FROM classmates WHERE address='서울';
-- DISTINCT : 중복 제거
SELECT DISTINCT address FROM classmates;

-- 데이터 삭제 : DELETE
-- 기본적으로 rowid를 기준으로 삭제
DELETE FROM classmates WHERE rowid=1

-- 데이터 수정 : UPDATE
UPDATE classmates
SET name='민찬우', address='서울'
WHERE rowid=5;

-- WHERE문 심화
SELECT *
FROM users
WHERE age>=30;

SELECT age, last_name
FROM users
WHERE age >= 30 and last_name='김';

-- Expressions (표현식)
-- COUNT
SELECT COUNT(*)
FROM users;
-- AVG
SELECT AVG(age)
FROM users
WHERE age>=30;
-- MAX
SELECT first_name,MAX(balance)
FROM users;

--LIKE
-- % 와 _
--20대인 사람 찾기
SELECT *
FROM users
WHERE age LIKE '2_';
-- 지역번호가 02 인 사람 찾기
SELECT *
FROM users
WHERE phone LIKE '02-%';

-- ORDER BY
-- ASC(ascending) DESC(descending)
SELECT *
FROM USERS
ORDER BY age ASC LIMIT 10;
-- ASC는 생략가능 defalt 값임
SELECT *
FROM USERS
ORDER BY age, last_name ASC LIMIT 10;

SELECT last_name, first_name
FROM users
ORDER BY balance DESC LIMIT 10;

--GROUP BY
SELECT last_name, COUNT(*) AS name_count
FROM users
GROUP BY last_name;

