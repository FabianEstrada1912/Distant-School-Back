

function chat(app,pool,ion){
    var users = [];

    ion.on("connection",function(socket){
        console.log("user conncected ",socket.id)
        socket.on("user_connect",function(username){
            users[username]= socket.id;
            ion.emit("user_connected",username)
            console.log("user conncected ",username)
        })

        socket.on("send_message",function(data){
          var socketID = users[data.receiver];
          console.log(socketID)
          ion.to(socketID).emit("new_message",data)
        })
    })
}

module.exports = chat;