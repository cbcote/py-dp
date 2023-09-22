import zlib
import bz2

# Define the Strategy interface
class CompressionStrategy:
    def compress(self, data: bytes) -> bytes:
        pass

    def decompress(self, compressed_data: bytes) -> bytes:
        pass

# Implement concrete strategies
class ZlibCompression(CompressionStrategy):
    def compress(self, data: bytes) -> bytes:
        return zlib.compress(data)

    def decompress(self, compressed_data: bytes) -> bytes:
        return zlib.decompress(compressed_data)

class Bz2Compression(CompressionStrategy):
    def compress(self, data: bytes) -> bytes:
        return bz2.compress(data)

    def decompress(self, compressed_data: bytes) -> bytes:
        return bz2.decompress(compressed_data)

# Context class
class Compressor:
    def __init__(self, strategy: CompressionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: CompressionStrategy):
        self._strategy = strategy

    def execute_compression(self, data: bytes) -> bytes:
        return self._strategy.compress(data)

    def execute_decompression(self, compressed_data: bytes) -> bytes:
        return self._strategy.decompress(compressed_data)


# Usage
data = b'This is some sample data for compression.'

# Using ZlibCompression
compressor = Compressor(ZlibCompression())
compressed_data = compressor.execute_compression(data)
decompressed_data = compressor.execute_decompression(compressed_data)
print('ZlibCompression - Original:', data)
print('ZlibCompression - Compressed:', compressed_data)
print('ZlibCompression - Decompressed:', decompressed_data)

# Switching to Bz2Compression
compressor.set_strategy(Bz2Compression())
compressed_data = compressor.execute_compression(data)
decompressed_data = compressor.execute_decompression(compressed_data)
print('\nBz2Compression - Original:', data)
print('Bz2Compression - Compressed:', compressed_data)
print('Bz2Compression - Decompressed:', decompressed_data)
