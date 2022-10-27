function processData(input) {
    // remove the metadata
    const [,k] = input.shift();
    
    // sort them by when they start
    input = input.sort((a,b) => {
       if(a[0] === b[0]) return a[1] - b[1];
       return a[0] - b[0];
    });
        
    const openings = [];
    let lastStop = [0,0];
    for(const schedule of input){
        // when does the meeting start?
        const start = schedule[0] + schedule[1];
        
        // how much time between end of last and start of current
        const window = start - (lastStop[0] + lastStop[1]);
        
        // there's enough time for one or more meetings
        if(window / k >= 1){
            openings.push([
                `${lastStop[0] / 60}`.padStart(2, '0'),
                `${lastStop[1]}`.padStart(2, '0'),
                `${schedule[0] / 60}`.padStart(2, '0'),
                `${schedule[1]}`.padStart(2, '0')
            ].join(' '));
        }
        
        // maybe scheduled meetings overlap. which one ends later?
        if(schedule[2] + schedule[3] > lastStop[0] + lastStop[1]) {
            lastStop = [schedule[2], schedule[3]];
        }
    }   
    
    // dont' forget about the end of the day
    const start = lastStop[0] + lastStop[1];
    const window = (24 * 60) - start;
    if(window !== 24 * 60 && window / k >= 1){
        openings.push([
            `${lastStop[0] / 60}`.padStart(2, '0'),
            `${lastStop[1]}`.padStart(2, '0'),
            `00`, `00`
        ].join(' '));
    }
    
    console.log(openings.join('\n'));
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    // i like working with arrays and numbers thank you very much
    _input = input.split('\n').map(l => l.split(' ').map((i, index) => Number.parseInt(i) * (index % 2 ? 1 : 60)));
});

process.stdin.on("end", function () {
   processData(_input);
});