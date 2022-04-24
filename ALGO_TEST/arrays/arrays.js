
/*
    Given a array of integers, return the indices of the two 
        numbers that add up to a given target.
*/

const match_target = function (myarray, target) {

    let v1 = 0
    let v2 = 1
    let valor_soma = 0

    while (valor_soma !== target) {

        valor_soma = myarray[v1] + myarray[v2]
        if (valor_soma == target) {

            console.log(" O valor foi encontrado = > ", valor_soma)
        }

        v1++
        v2++

    }
}


let myarray = [1, 3, 7, 9, 2]

let target = 11

match_target(myarray, target)
