import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button.jsx'
import { Input } from '@/components/ui/input.jsx'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Send, Bot, User, Settings, Wrench } from 'lucide-react'
import './App.css'

const API_BASE_URL = 'https://5000-iyb9gafuiflmzfk2fkwnf-195ef904.manusvm.computer'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [isProcessing, setIsProcessing] = useState(false)
  const [agentStatus, setAgentStatus] = useState(null)
  const [availableTools, setAvailableTools] = useState([])

  useEffect(() => {
    // Load agent status and tools on component mount
    loadAgentStatus()
    loadAvailableTools()
  }, [])

  const loadAgentStatus = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/status`)
      const data = await response.json()
      if (data.success) {
        setAgentStatus(data.data)
      }
    } catch (error) {
      console.error('Failed to load agent status:', error)
    }
  }

  const loadAvailableTools = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/api/tools`)
      const data = await response.json()
      if (data.success) {
        setAvailableTools(data.tools)
      }
    } catch (error) {
      console.error('Failed to load tools:', error)
    }
  }

  const handleSend = async () => {
    if (!input.trim()) return

    const userMessage = { role: 'user', content: input }
    setMessages(prev => [...prev, userMessage])
    setInput('')
    setIsProcessing(true)

    try {
      const response = await fetch(`${API_BASE_URL}/api/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage.content })
      })

      const data = await response.json()
      
      if (data.success) {
        const agentMessage = { 
          role: 'agent', 
          content: data.response,
          tool_used: data.tool_used
        }
        setMessages(prev => [...prev, agentMessage])
        
        // Update status after processing
        loadAgentStatus()
      } else {
        const errorMessage = { 
          role: 'agent', 
          content: `错误: ${data.error || '处理消息时发生未知错误'}`,
          isError: true
        }
        setMessages(prev => [...prev, errorMessage])
      }
    } catch (error) {
      const errorMessage = { 
        role: 'agent', 
        content: `连接错误: ${error.message}`,
        isError: true
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsProcessing(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-4 gap-4">
        
        {/* Sidebar */}
        <div className="lg:col-span-1 space-y-4">
          {/* Agent Status */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-sm">
                <Settings className="w-4 h-4" />
                Agent 状态
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              {agentStatus ? (
                <>
                  <div className="flex justify-between text-sm">
                    <span>可用工具:</span>
                    <Badge variant="secondary">{agentStatus.tools_available}</Badge>
                  </div>
                  <div className="flex justify-between text-sm">
                    <span>上下文长度:</span>
                    <Badge variant="secondary">{agentStatus.context_length}</Badge>
                  </div>
                </>
              ) : (
                <div className="text-sm text-gray-500">加载中...</div>
              )}
            </CardContent>
          </Card>

          {/* Available Tools */}
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-sm">
                <Wrench className="w-4 h-4" />
                可用工具
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                {availableTools.map((tool, index) => (
                  <div key={index} className="text-xs">
                    <div className="font-medium">{tool.name}</div>
                    <div className="text-gray-500">{tool.description}</div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Main Chat Area */}
        <div className="lg:col-span-3">
          <Card className="h-[80vh] flex flex-col">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Bot className="w-6 h-6 text-blue-600" />
                Manus Replica - AI Agent
                <Badge variant="outline" className="ml-auto">Web版本</Badge>
              </CardTitle>
            </CardHeader>
            
            <CardContent className="flex-1 flex flex-col">
              {/* Messages Area */}
              <div className="flex-1 overflow-y-auto mb-4 space-y-4">
                {messages.length === 0 && (
                  <div className="text-center text-gray-500 mt-8">
                    <Bot className="w-12 h-12 mx-auto mb-4 text-gray-400" />
                    <p>欢迎使用 Manus Replica！发送消息开始对话。</p>
                    <div className="mt-4 text-sm">
                      <p>尝试发送包含以下关键词的消息：</p>
                      <div className="flex gap-2 justify-center mt-2">
                        <Badge variant="outline">文件</Badge>
                        <Badge variant="outline">命令</Badge>
                        <Badge variant="outline">shell</Badge>
                      </div>
                    </div>
                  </div>
                )}
                
                {messages.map((message, index) => (
                  <div
                    key={index}
                    className={`flex gap-3 ${
                      message.role === 'user' ? 'justify-end' : 'justify-start'
                    }`}
                  >
                    <div
                      className={`flex gap-3 max-w-[80%] ${
                        message.role === 'user' ? 'flex-row-reverse' : 'flex-row'
                      }`}
                    >
                      <div className="w-8 h-8 rounded-full flex items-center justify-center bg-gray-200">
                        {message.role === 'user' ? (
                          <User className="w-4 h-4" />
                        ) : (
                          <Bot className="w-4 h-4 text-blue-600" />
                        )}
                      </div>
                      <div
                        className={`p-3 rounded-lg ${
                          message.role === 'user'
                            ? 'bg-blue-600 text-white'
                            : message.isError
                            ? 'bg-red-100 text-red-800 border border-red-200'
                            : 'bg-gray-100 text-gray-800'
                        }`}
                      >
                        <div className="whitespace-pre-wrap">{message.content}</div>
                        {message.tool_used && (
                          <div className="mt-2 pt-2 border-t border-gray-300">
                            <Badge variant="secondary" className="text-xs">
                              使用工具: {message.tool_used}
                            </Badge>
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
                
                {isProcessing && (
                  <div className="flex gap-3 justify-start">
                    <div className="w-8 h-8 rounded-full flex items-center justify-center bg-gray-200">
                      <Bot className="w-4 h-4 text-blue-600" />
                    </div>
                    <div className="bg-gray-100 text-gray-800 p-3 rounded-lg">
                      <div className="flex gap-1">
                        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                        <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                      </div>
                    </div>
                  </div>
                )}
              </div>

              {/* Input Area */}
              <div className="flex gap-2">
                <Input
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  placeholder="输入您的消息..."
                  onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                  disabled={isProcessing}
                  className="flex-1"
                />
                <Button 
                  onClick={handleSend} 
                  disabled={isProcessing || !input.trim()}
                  className="px-4"
                >
                  <Send className="w-4 h-4" />
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}

export default App

