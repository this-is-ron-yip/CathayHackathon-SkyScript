import React, { useState } from "react";
import axios from "axios";

const Chat = () => {
  const [messages, setMessages] = useState([]); // State to store the messages
  const [currentSender, setCurrentSender] = useState("human"); // State to store the current sender
  const user = { _id: "human", name: "You" }; // User data
  const chatbot = { _id: "ai", name: "AI Chatbot" }; // Chatbot data

  const handleSendMessage = async (e) => {
    e.preventDefault();
    const messageInput = e.target.elements.message;
    const messageText = messageInput.value.trim();
  
    if (messageText !== "") {
      const newMessage = {
        role: currentSender === "human" ? "human" : "assistant",
        content: messageText,
      };
  
      setMessages([...messages, newMessage]);
      messageInput.value = "";
  
      try {
        const response = await axios.post("http://127.0.0.1:5000/chat", [
          ...messages,
          newMessage,
        ]);
  
        const chatbotReply = {
          role: "assistant",
          content: response.data,
        };
  
        setMessages([...messages, newMessage, chatbotReply]);
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  return (
    <div className="flex flex-col h-screen w-screen bg-gray-200 max-w-[390px] mx-auto">
      <div className="bg-teal-500 text-white p-4 font-bold text-2xl text-center">
        GatherGo 集遊
      </div>
      <div className="flex-grow mx-2 overflow-y-auto h-[calc(100vh-168px)]">
        {messages.map((message) => (
          <div
            key={message._id}
            className={`my-2 p-2 rounded ${
              message.role === "human"
                ? "bg-green-200 self-end"
                : "bg-white self-start"
            }`}
          >
            <div className="font-bold">{message.role}</div>
            {message.content}
          </div>
        ))}
      </div>

      <div className="flex flex-col items-center justify-between mb-4">
        <form onSubmit={handleSendMessage} className="w-full px-4">
          <div className="flex">
            <input
              type="text"
              name="message"
              placeholder="Enter your message here"
              className="text-lg border border-gray-300 rounded-l p-2 flex-1"
            />
            <button
              type="submit"
              className="text-lg border rounded-r p-2 bg-teal-500 text-white"
            >
              Send
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Chat;