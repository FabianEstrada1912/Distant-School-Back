

function chat(app,pool,io){
    
    let userList = new Map();
    
    io.on('connection', (socket) => {
        let userName = socket.handshake.query.userName;
        let friends = socket.handshake.query.friends;
        addUser(userName,friends,socket.id);
        socket.broadcast.emit('user-list', [...userList.keys()]);
        socket.emit('user-list', [...userList.keys()]);
    
        socket.on('message', (msg) => {
            socket.broadcast.emit('message-broadcast', {message: msg, userName: userName,friends:friends});
        })
    
        socket.on('disconnect', (reason) => {
            removeUser(socket.handshake.query.userName, socket.handshake.query.friends, socket.id);
        })
    });
    
    function addUser(userName,friends,id) {
        if (!userList.has(userName)) {
            userList.set(userName, new Set(id,friends));
        } else {
            userList.get(userName).add(id,friends);
        }
    }
    
    function removeUser(userName,friends,id) {
        if (userList.has(userName)) {
            let userIds = userList.get(userName);
            if (userIds.size == 0) {
                userList.delete(userName);
            }
        }
    }
}
module.exports = chat;