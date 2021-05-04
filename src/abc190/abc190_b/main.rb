gets.split.map(&:to_i).tap{|n, s, d|
    puts (0...n).to_a.map {|i|
        gets.split.map(&:to_i).tap {|(x, y)| 
            break (x < s && d < y) }}.any? {|t| t} ? 'Yes' : 'No'
        }