impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = Vec::new();

        for token in tokens {
            match token.as_str() {
                "+" | "-" | "*" | "/" => {
                    let op2 = stack.pop().unwrap();
                    let op1 = stack.pop().unwrap();

                    match token.as_str() {
                        "+" => stack.push(op1 + op2),
                        "-" => stack.push(op1 - op2),
                        "*" => stack.push(op1 * op2),
                        "/" => stack.push(op1 / op2),
                        _ => continue,
                    }
                },
                _ => stack.push(token.parse::<i32>().unwrap()),
            }
        }
        stack[0]
    }
}
