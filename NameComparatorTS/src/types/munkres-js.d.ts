declare module 'munkres-js' {
    type Matrix = number[][];
    type ResultPair = [number, number];

    function computeMunkres(cost_matrix: Matrix): ResultPair[];

    export default munkres;
}