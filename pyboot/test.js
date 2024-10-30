const spawn = require('cross-spawn');

// 异步生成子进程，运行npm命令
const child = spawn('npm', ['list', '-g', '-depth', '0'], { stdio: 'inherit' });

// 同步生成子进程，运行npm命令
const result = spawn.sync('npm', ['list', '-g', '-depth', '0'], { stdio: 'inherit' });

// 考虑个人是服务器的超集合