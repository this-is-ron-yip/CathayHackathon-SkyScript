import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from 'react-router-dom';

const Chat = () => {
  const [messages, setMessages] = useState([]); // State to store the messages
  const [messageInput, setMessageInput] = useState(''); // State for the input field
  const navigate = useNavigate();

  const handleSendMessage = async (e) => {
    e.preventDefault();
    const messageText = messageInput.trim();

    if (messageText !== "") {
      const newMessage = {
        role: "user",
        content: messageText,
      };

      setMessages((prevMessages) => [...prevMessages, newMessage]);
      setMessageInput("");

      try {
        // First, send the message to the /chat endpoint
        const chatResponse = await axios.post("http://127.0.0.1:5000/chat", [
          ...messages,
          newMessage,
        ]);

        // The chatResponse.data contains the requirement data
        const requirementData = chatResponse.data;

        // Set the assistant's reply in the chat (you can customize the content)
        const chatbotReply = {
          role: "assistant",
          content: `Received requirements: ${JSON.stringify(requirementData)}`, 
        };

        setMessages((prevMessages) => [...prevMessages, chatbotReply]);

        // Now, send the requirementData to the /route endpoint
        const routeResponse = await axios.post("http://127.0.0.1:5000/route", requirementData);

        const routeData = routeResponse.data;

        console.log("Route Data: ", routeData);

        // Navigate to the maps page with the routeData
        navigate('/maps', { state: { routeData } });

      } catch (error) {
        console.error("Error:", error);
        // Handle the error, e.g., display an error message to the user
      }
    }
  };

  return (
    <div className="flex flex-col h-screen w-screen bg-gray-200 max-w-[390px] mx-auto">
      <div className="bg-teal-500 text-white p-4 font-bold text-2xl text-center">
        GatherGo 集遊
      </div>
      <div className="flex-grow mx-2 overflow-y-auto h-[calc(100vh-168px)]">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`my-2 p-2 rounded ${
              message.role === "user"
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
              value={messageInput}
              onChange={(e) => setMessageInput(e.target.value)}
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