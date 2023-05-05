use petgraph::unionfind::UnionFind;
use proconio::{input, marker::Usize1};

struct Edge(usize, usize, usize, i32);

fn main() {
    input! {
        n: usize,
        m: usize,
        mut v: [(Usize1, Usize1, i32); m]
    }
    let mut v: Vec<Edge> = v
        .into_iter()
        .enumerate()
        .map(|(i, (a, b, c))| Edge(a, b, i + 1, c))
        .collect();

    let mut ans: Vec<u32> = Vec::new();
    v.sort_by_key(|e| e.3);

    let mut uf = UnionFind::new(n);
    for i in (0..m).rev() {
        if !uf.equiv(v[i].0, v[i].1) {
            uf.union(v[i].0, v[i].1);
            ans.push(v[i].2 as u32);
        }
    }
    ans.sort();
    for i in ans.iter() {
        println!("{}", i);
    }
}
