class Submarine
  @@zeros = []
  @@ones = []

  def read_binary(binary)
    for i in 0..(binary.length-1) do
      if binary[i].to_i == 0 then
        @@zeros[i] = @@zeros[i] + 1
      else
        @@ones[i] = @@ones[i] + 1
      end
    end
    return binary
  end
end

submarine = Submarine.new()
print submarine.read_binary("01101100")

